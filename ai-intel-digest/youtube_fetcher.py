#!/usr/bin/env python3
"""
YouTube Transcript Fetcher using yt-dlp.
Fetches transcripts from configured channels for the last 30 days.
"""

import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from pathlib import Path

MIN_TRANSCRIPT_CHARS = 500
TRANSCRIPT_WORKERS = 8


def load_sources(config_path: str) -> dict:
    """Load YouTube sources from config file."""
    with open(config_path) as f:
        return json.load(f)


def get_date_cutoff() -> str:
    """Get the date cutoff (30 days ago in YYYYMMDD format)."""
    date_30_days_ago = datetime.now() - timedelta(days=30)
    return date_30_days_ago.strftime("%Y%m%d")


def fetch_channel_videos(channel_id: str, date_cutoff: str, max_videos: int = 50) -> list[dict]:
    """
    Fetch video metadata from a YouTube channel.
    Uses JSON output to get proper metadata including upload dates.
    """
    videos = []

    # Use --dump-json to get proper metadata, limit playlist items
    cmd = [
        "yt-dlp",
        "--dump-json",
        "--flat-playlist",
        "--playlist-end", str(max_videos),  # Limit to recent videos
        f"https://www.youtube.com/{channel_id}/videos"
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print(f"  Warning: Could not list videos for {channel_id}: {result.stderr[:200]}")
            return videos

        # Each line is a JSON object
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            try:
                data = json.loads(line)
                video_id = data.get("id", "")
                title = data.get("title", "Untitled")
                upload_date = data.get("upload_date", "")

                # Filter by date - only include if within date range
                if upload_date and upload_date >= date_cutoff:
                    videos.append({
                        "id": video_id,
                        "title": title,
                        "upload_date": upload_date
                    })
                elif not upload_date:
                    # If no date, include but mark as unknown
                    videos.append({
                        "id": video_id,
                        "title": title,
                        "upload_date": "unknown"
                    })
            except json.JSONDecodeError:
                continue

    except subprocess.TimeoutExpired:
        print(f"  Timeout listing videos for {channel_id}")
    except Exception as e:
        print(f"  Error listing videos for {channel_id}: {e}")

    return videos


def fetch_playlist_videos(playlist_id: str, date_cutoff: str, max_videos: int = 30) -> list[dict]:
    """Fetch videos from a playlist with proper date filtering."""
    videos = []

    cmd = [
        "yt-dlp",
        "--dump-json",
        "--flat-playlist",
        "--playlist-end", str(max_videos),
        f"https://www.youtube.com/playlist?list={playlist_id}"
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print(f"  Warning: Could not list playlist {playlist_id}")
            return videos

        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            try:
                data = json.loads(line)
                video_id = data.get("id", "")
                title = data.get("title", "Untitled")
                upload_date = data.get("upload_date", "")

                if upload_date and upload_date >= date_cutoff:
                    videos.append({
                        "id": video_id,
                        "title": title,
                        "upload_date": upload_date
                    })
                elif not upload_date:
                    videos.append({
                        "id": video_id,
                        "title": title,
                        "upload_date": "unknown"
                    })
            except json.JSONDecodeError:
                continue

    except Exception as e:
        print(f"  Error listing playlist {playlist_id}: {e}")

    return videos


def fetch_transcript(video_id: str, output_dir: Path) -> str | None:
    """
    Fetch transcript/subtitles for a single video.
    Returns the transcript text or None if unavailable.
    """
    # Try to get auto-generated or manual subtitles
    cmd = [
        "yt-dlp",
        "--write-auto-sub",
        "--write-sub",
        "--sub-lang", "en",
        "--skip-download",
        "--sub-format", "vtt",
        "-o", str(output_dir / "%(id)s"),
        f"https://www.youtube.com/watch?v={video_id}"
    ]

    try:
        subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        # Look for the subtitle file
        vtt_files = list(output_dir.glob(f"{video_id}*.vtt"))
        if vtt_files:
            # Convert VTT to plain text
            transcript = parse_vtt(vtt_files[0])
            # Clean up VTT file
            vtt_files[0].unlink()
            return transcript
    except subprocess.TimeoutExpired:
        print(f"    Timeout fetching transcript for {video_id}")
    except Exception as e:
        print(f"    Error fetching transcript for {video_id}: {e}")

    return None


def parse_vtt(vtt_path: Path) -> str:
    """Parse VTT subtitle file and extract plain text."""
    lines = []
    with open(vtt_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Skip VTT headers, timestamps, and empty lines
            if not line:
                continue
            if line.startswith("WEBVTT"):
                continue
            if line.startswith("Kind:") or line.startswith("Language:"):
                continue
            if "-->" in line:
                continue
            if line.startswith("NOTE"):
                continue
            # Skip position/alignment tags
            if line.startswith("<") and line.endswith(">"):
                continue
            # Remove inline tags like <c> </c>
            clean_line = re.sub(r"<[^>]+>", "", line)
            if clean_line:
                lines.append(clean_line)

    # Remove duplicate consecutive lines (common in auto-subs)
    deduped = []
    for line in lines:
        if not deduped or line != deduped[-1]:
            deduped.append(line)

    return " ".join(deduped)


def main(config_path: str, output_dir: str) -> dict:
    """
    Main function to fetch all YouTube transcripts.
    Returns summary of fetched content.
    """
    config = load_sources(config_path)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    date_cutoff = get_date_cutoff()
    print(f"Fetching YouTube content from {date_cutoff} onwards...")

    summary = {
        "channels_processed": 0,
        "videos_found": 0,
        "transcripts_fetched": 0,
        "errors": []
    }

    all_videos = []

    # Process all channel categories with appropriate limits
    category_limits = {
        "daily": 35,    # ~30 days of daily content + buffer
        "weekly": 10,   # ~4-5 weeks of weekly content
        "monthly": 10   # Recent monthly content
    }

    for category in ["daily", "weekly", "monthly"]:
        max_videos = category_limits.get(category, 30)

        for source in config.get(category, []):
            name = source["name"]
            print(f"\nProcessing: {name} (checking last {max_videos} videos)")

            if "playlist_id" in source:
                videos = fetch_playlist_videos(source["playlist_id"], date_cutoff, max_videos)
            elif "channel_id" in source:
                videos = fetch_channel_videos(source["channel_id"], date_cutoff, max_videos)
            else:
                print(f"  Skipping {name}: no channel_id or playlist_id")
                continue

            summary["channels_processed"] += 1
            print(f"  Found {len(videos)} videos in date range")

            for video in videos:
                video["source"] = name
                all_videos.append(video)
                summary["videos_found"] += 1

    # Fetch transcripts in parallel
    print(f"\n\nFetching transcripts for {len(all_videos)} videos ({TRANSCRIPT_WORKERS} workers)...")
    summary["short_transcripts_dropped"] = 0

    def _fetch(video):
        return video, fetch_transcript(video["id"], output_path)

    with ThreadPoolExecutor(max_workers=TRANSCRIPT_WORKERS) as executor:
        futures = [executor.submit(_fetch, v) for v in all_videos]
        for i, future in enumerate(as_completed(futures), 1):
            video, transcript = future.result()
            print(f"  [{i}/{len(all_videos)}] {video['title'][:50]}")
            if transcript and len(transcript) >= MIN_TRANSCRIPT_CHARS:
                video["transcript"] = transcript
                summary["transcripts_fetched"] += 1
            elif transcript:
                video["transcript"] = None
                summary["short_transcripts_dropped"] += 1
                summary["errors"].append(f"Short transcript dropped: {video['title']}")
            else:
                video["transcript"] = None
                summary["errors"].append(f"No transcript: {video['title']}")

    # Save combined output
    output_file = output_path / "youtube_content.json"
    with open(output_file, "w") as f:
        json.dump({
            "fetched_at": datetime.now().isoformat(),
            "date_range": f"{date_cutoff} to {datetime.now().strftime('%Y%m%d')}",
            "videos": all_videos
        }, f, indent=2)

    print(f"\n\nSummary:")
    print(f"  Channels processed: {summary['channels_processed']}")
    print(f"  Videos found: {summary['videos_found']}")
    print(f"  Transcripts fetched: {summary['transcripts_fetched']}")
    print(f"  Short transcripts dropped (<{MIN_TRANSCRIPT_CHARS} chars): {summary['short_transcripts_dropped']}")
    print(f"  Output saved to: {output_file}")

    return summary


if __name__ == "__main__":
    config = sys.argv[1] if len(sys.argv) > 1 else "~/assistant/context/youtube_sources.json"
    output = sys.argv[2] if len(sys.argv) > 2 else "~/assistant/content/ai-intel/sources/youtube"

    config = str(Path(config).expanduser())
    output = str(Path(output).expanduser())

    main(config, output)
