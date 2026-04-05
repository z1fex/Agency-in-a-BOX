#!/usr/bin/env python3
"""
Content Calendar Generator

Generates a blank content calendar CSV for the next N days.
Pre-populated with dates, day names, and empty columns for content planning.

Usage:
    python generate-calendar.py
    python generate-calendar.py --days 30
    python generate-calendar.py --days 90 --output calendar.csv
    python generate-calendar.py --days 30 --start 2025-02-01
    python generate-calendar.py --days 30 --platforms "LinkedIn,Twitter,Instagram"
    python generate-calendar.py --days 30 --markdown
"""

import csv
import sys
import argparse
from datetime import datetime, timedelta


DEFAULT_PLATFORMS = ["LinkedIn", "Twitter/X", "Instagram", "Blog", "Newsletter"]

CONTENT_TYPES = {
    "LinkedIn": ["Text Post", "Carousel", "Poll", "Article", "Video"],
    "Twitter/X": ["Tweet", "Thread", "Poll", "Quote Tweet"],
    "Instagram": ["Feed Post", "Carousel", "Reel", "Story"],
    "Blog": ["How-to", "Listicle", "Case Study", "Thought Leadership", "Comparison"],
    "Newsletter": ["Weekly Digest", "Feature Story", "Curated Links", "Product Update"],
    "Facebook": ["Post", "Story", "Reel", "Live", "Event"],
    "TikTok": ["Short Video", "Stitch", "Duet", "Trending"],
    "YouTube": ["Long-form", "Shorts", "Community Post"],
}


def generate_calendar(days, start_date=None, platforms=None, include_weekends=True):
    """Generate calendar rows for the specified number of days."""
    if start_date:
        current = datetime.strptime(start_date, "%Y-%m-%d")
    else:
        current = datetime.now()

    if platforms is None:
        platforms = DEFAULT_PLATFORMS

    rows = []
    day_count = 0

    while day_count < days:
        day_name = current.strftime("%A")

        # Skip weekends if requested
        if not include_weekends and day_name in ("Saturday", "Sunday"):
            current += timedelta(days=1)
            continue

        date_str = current.strftime("%Y-%m-%d")
        week_num = current.isocalendar()[1]

        row = {
            "Week": f"W{week_num}",
            "Date": date_str,
            "Day": day_name,
            "Platform": "",
            "Content Type": "",
            "Topic": "",
            "Headline/Hook": "",
            "Keywords": "",
            "Pillar": "",
            "Funnel Stage": "",
            "CTA": "",
            "Media Needed": "",
            "Status": "Planned",
            "Notes": "",
        }
        rows.append(row)
        day_count += 1
        current += timedelta(days=1)

    return rows


def to_csv(rows, output_file):
    """Write rows to CSV file."""
    if not rows:
        return

    fieldnames = list(rows[0].keys())
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def to_markdown(rows):
    """Convert rows to a markdown table string."""
    if not rows:
        return "*(No data)*"

    headers = list(rows[0].keys())

    # Calculate column widths
    col_widths = {h: len(h) for h in headers}
    for row in rows:
        for h in headers:
            col_widths[h] = max(col_widths[h], len(str(row.get(h, ""))))

    # Build table
    lines = []
    header_line = "| " + " | ".join(h.ljust(col_widths[h]) for h in headers) + " |"
    separator = "|" + "|".join("-" * (col_widths[h] + 2) for h in headers) + "|"
    lines.append(header_line)
    lines.append(separator)

    for row in rows:
        cells = [str(row.get(h, "")).ljust(col_widths[h]) for h in headers]
        lines.append("| " + " | ".join(cells) + " |")

    return "\n".join(lines)


def print_summary(rows, platforms):
    """Print a summary of the generated calendar."""
    if not rows:
        return

    first_date = rows[0]["Date"]
    last_date = rows[-1]["Date"]
    weeks = len(set(r["Week"] for r in rows))
    weekdays = sum(1 for r in rows if r["Day"] not in ("Saturday", "Sunday"))
    weekends = len(rows) - weekdays

    print(f"\nCalendar Summary")
    print(f"{'=' * 40}")
    print(f"Period:        {first_date} to {last_date}")
    print(f"Total days:    {len(rows)}")
    print(f"Weekdays:      {weekdays}")
    print(f"Weekend days:  {weekends}")
    print(f"Weeks:         {weeks}")
    print(f"Platforms:     {', '.join(platforms)}")
    print()
    print("Suggested content types per platform:")
    for platform in platforms:
        types = CONTENT_TYPES.get(platform, ["General"])
        print(f"  {platform}: {', '.join(types)}")
    print()
    print("Status options: Planned | Brief | Draft | Review | Ready | Published | Promoted")
    print("Funnel stages: TOFU (Awareness) | MOFU (Consideration) | BOFU (Decision)")


def main():
    parser = argparse.ArgumentParser(description="Generate a blank content calendar")
    parser.add_argument("--days", type=int, default=30, help="Number of days (default: 30)")
    parser.add_argument("--start", type=str, default=None, help="Start date YYYY-MM-DD (default: today)")
    parser.add_argument("--output", type=str, default="content-calendar.csv", help="Output CSV file (default: content-calendar.csv)")
    parser.add_argument("--platforms", type=str, default=None, help="Comma-separated platforms (default: LinkedIn,Twitter/X,Instagram,Blog,Newsletter)")
    parser.add_argument("--no-weekends", action="store_true", help="Exclude weekends")
    parser.add_argument("--markdown", action="store_true", help="Output as markdown table instead of CSV")

    args = parser.parse_args()

    platforms = [p.strip() for p in args.platforms.split(",")] if args.platforms else DEFAULT_PLATFORMS

    try:
        rows = generate_calendar(
            days=args.days,
            start_date=args.start,
            platforms=platforms,
            include_weekends=not args.no_weekends,
        )
    except ValueError as e:
        print(f"Error: {e}")
        print("Date format should be YYYY-MM-DD")
        sys.exit(1)

    if args.markdown:
        print(to_markdown(rows))
    else:
        to_csv(rows, args.output)
        print(f"Calendar written to {args.output}")
        print_summary(rows, platforms)


if __name__ == "__main__":
    main()
