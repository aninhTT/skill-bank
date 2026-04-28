#!/usr/bin/env python3
"""
Newsletter Fetcher for AI Intel Digest.
Fetches content from RSS feeds and web scraping for the last 30 days.
Uses only stdlib (no external dependencies).
"""

import json
import sys
import urllib.request
import urllib.error
import ssl
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET


class HTMLTextExtractor(HTMLParser):
    """Extract plain text from HTML content."""

    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.skip_tags = {"script", "style", "noscript"}
        self.current_skip = False

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.current_skip = True
        elif tag in ("p", "br", "div", "h1", "h2", "h3", "h4", "h5", "h6", "li"):
            self.text_parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.current_skip = False

    def handle_data(self, data):
        if not self.current_skip:
            self.text_parts.append(data)

    def get_text(self):
        return " ".join("".join(self.text_parts).split())


def html_to_text(html: str) -> str:
    """Convert HTML to plain text."""
    parser = HTMLTextExtractor()
    try:
        parser.feed(html)
        return parser.get_text()
    except Exception:
        # Fallback: strip tags with regex-like approach
        import re
        text = re.sub(r"<[^>]+>", " ", html)
        return " ".join(text.split())


def fetch_url(url: str, timeout: int = 30) -> str | None:
    """Fetch URL content with proper headers."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }

    # Create SSL context that doesn't verify (some feeds have cert issues)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as response:
            return response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        print(f"    HTTP Error {e.code}: {url}")
    except urllib.error.URLError as e:
        print(f"    URL Error: {e.reason}")
    except Exception as e:
        print(f"    Error fetching {url}: {e}")

    return None


def parse_date(date_str: str) -> datetime | None:
    """Parse various date formats from RSS feeds."""
    if not date_str:
        return None

    # Try RFC 2822 format (common in RSS)
    try:
        return parsedate_to_datetime(date_str)
    except Exception:
        pass

    # Try ISO format
    for fmt in [
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%d",
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S GMT",
    ]:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    return None


def is_within_date_range(pub_date: datetime | None, days: int = 30) -> bool:
    """Check if publication date is within the last N days."""
    if pub_date is None:
        return True  # Include if we can't determine date

    cutoff = datetime.now(pub_date.tzinfo) if pub_date.tzinfo else datetime.now()
    cutoff = cutoff - timedelta(days=days)

    return pub_date >= cutoff


def fetch_rss_feed(feed_url: str, source_name: str, days: int = 30) -> list[dict]:
    """Fetch and parse RSS feed, returning items within date range."""
    items = []

    content = fetch_url(feed_url)
    if not content:
        return items

    try:
        root = ET.fromstring(content)
    except ET.ParseError as e:
        print(f"    XML Parse Error: {e}")
        return items

    # Handle both RSS and Atom feeds
    namespaces = {
        "atom": "http://www.w3.org/2005/Atom",
        "content": "http://purl.org/rss/1.0/modules/content/"
    }

    # Try RSS format first
    for item in root.findall(".//item"):
        title_el = item.find("title")
        link_el = item.find("link")
        pub_date_el = item.find("pubDate")
        desc_el = item.find("description")
        content_el = item.find("content:encoded", namespaces)

        title = title_el.text if title_el is not None else "Untitled"
        link = link_el.text if link_el is not None else ""
        pub_date_str = pub_date_el.text if pub_date_el is not None else ""
        pub_date = parse_date(pub_date_str)

        if not is_within_date_range(pub_date, days):
            continue

        # Prefer full content over description
        if content_el is not None and content_el.text:
            content_text = html_to_text(content_el.text)
        elif desc_el is not None and desc_el.text:
            content_text = html_to_text(desc_el.text)
        else:
            content_text = ""

        items.append({
            "title": title,
            "link": link,
            "pub_date": pub_date.isoformat() if pub_date else None,
            "content": content_text,
            "source": source_name
        })

    # Try Atom format if no RSS items found
    if not items:
        for entry in root.findall(".//atom:entry", namespaces) or root.findall(".//entry"):
            title_el = entry.find("atom:title", namespaces) or entry.find("title")
            link_el = entry.find("atom:link", namespaces) or entry.find("link")
            pub_el = entry.find("atom:published", namespaces) or entry.find("published") or entry.find("atom:updated", namespaces) or entry.find("updated")
            content_el = entry.find("atom:content", namespaces) or entry.find("content")
            summary_el = entry.find("atom:summary", namespaces) or entry.find("summary")

            title = title_el.text if title_el is not None else "Untitled"

            # Atom links can be in href attribute
            if link_el is not None:
                link = link_el.get("href") or link_el.text or ""
            else:
                link = ""

            pub_date_str = pub_el.text if pub_el is not None else ""
            pub_date = parse_date(pub_date_str)

            if not is_within_date_range(pub_date, days):
                continue

            if content_el is not None and content_el.text:
                content_text = html_to_text(content_el.text)
            elif summary_el is not None and summary_el.text:
                content_text = html_to_text(summary_el.text)
            else:
                content_text = ""

            items.append({
                "title": title,
                "link": link,
                "pub_date": pub_date.isoformat() if pub_date else None,
                "content": content_text,
                "source": source_name
            })

    return items


def scrape_the_batch(url: str, days: int = 30) -> list[dict]:
    """
    Scrape The Batch from deeplearning.ai.
    This is a simple scraper that gets article links from the main page.
    """
    items = []

    content = fetch_url(url)
    if not content:
        return items

    # Extract article links from the page
    import re

    # Find article links - The Batch uses paths like /the-batch/issue-XXX/
    article_pattern = r'href="(/the-batch/[^"]+)"'
    links = re.findall(article_pattern, content)
    links = list(set(links))  # Dedupe

    print(f"    Found {len(links)} article links")

    # Fetch each article (limit to avoid overloading)
    for link in links[:10]:
        full_url = f"https://www.deeplearning.ai{link}"
        article_content = fetch_url(full_url)

        if not article_content:
            continue

        # Extract title
        title_match = re.search(r"<h1[^>]*>([^<]+)</h1>", article_content)
        title = title_match.group(1) if title_match else link.split("/")[-2]

        # Extract main content (simplified)
        text = html_to_text(article_content)

        # Truncate if too long
        if len(text) > 5000:
            text = text[:5000] + "..."

        items.append({
            "title": title,
            "link": full_url,
            "pub_date": None,  # Would need to parse from page
            "content": text,
            "source": "The Batch"
        })

    return items


def load_config(config_path: str) -> dict:
    """Load newsletter sources config."""
    with open(config_path) as f:
        return json.load(f)


def main(config_path: str, output_dir: str) -> dict:
    """
    Main function to fetch all newsletter content.
    Returns summary of fetched content.
    """
    config = load_config(config_path)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print("Fetching newsletter content from last 30 days...")

    summary = {
        "feeds_processed": 0,
        "items_fetched": 0,
        "errors": []
    }

    all_items = []

    # Process RSS feeds
    for feed in config.get("rss_feeds", []):
        name = feed["name"]
        url = feed["url"]
        print(f"\nProcessing RSS: {name}")

        items = fetch_rss_feed(url, name)
        print(f"  Found {len(items)} items in date range")

        all_items.extend(items)
        summary["feeds_processed"] += 1
        summary["items_fetched"] += len(items)

    # Process web scrape sources
    for source in config.get("web_scrape", []):
        name = source["name"]
        url = source["url"]
        print(f"\nScraping: {name}")

        if "deeplearning.ai" in url:
            items = scrape_the_batch(url)
        else:
            print(f"  Skipping {name}: no scraper implemented")
            continue

        print(f"  Found {len(items)} items")

        all_items.extend(items)
        summary["feeds_processed"] += 1
        summary["items_fetched"] += len(items)

    # Save combined output
    output_file = output_path / "newsletter_content.json"
    with open(output_file, "w") as f:
        json.dump({
            "fetched_at": datetime.now().isoformat(),
            "items": all_items
        }, f, indent=2)

    print(f"\n\nSummary:")
    print(f"  Feeds processed: {summary['feeds_processed']}")
    print(f"  Items fetched: {summary['items_fetched']}")
    print(f"  Output saved to: {output_file}")

    return summary


if __name__ == "__main__":
    config = sys.argv[1] if len(sys.argv) > 1 else "~/assistant/context/newsletter_sources.json"
    output = sys.argv[2] if len(sys.argv) > 2 else "~/assistant/content/ai-intel/sources/newsletters"

    config = str(Path(config).expanduser())
    output = str(Path(output).expanduser())

    main(config, output)
