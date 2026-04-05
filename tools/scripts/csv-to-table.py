#!/usr/bin/env python3
"""
CSV to Markdown Table Converter

Reads a CSV file and outputs a formatted markdown table.

Usage:
    python csv-to-table.py input.csv
    python csv-to-table.py input.csv --max-rows 20
    python csv-to-table.py input.csv --columns "Name,Email,Status"
    python csv-to-table.py input.csv --output output.md
    python csv-to-table.py input.csv --align left,center,right
"""

import csv
import sys
import argparse


def csv_to_markdown(input_file, max_rows=None, columns=None, alignments=None):
    """Convert a CSV file to a markdown table string."""
    with open(input_file, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        all_rows = list(reader)

    if not all_rows:
        return "*(Empty CSV file)*"

    # Select columns
    if columns:
        headers = [c.strip() for c in columns.split(",")]
        # Validate columns exist
        available = list(all_rows[0].keys())
        for h in headers:
            if h not in available:
                print(f"Warning: Column '{h}' not found. Available: {', '.join(available)}")
                headers.remove(h)
    else:
        headers = list(all_rows[0].keys())

    # Limit rows
    rows = all_rows[:max_rows] if max_rows else all_rows
    truncated = len(all_rows) - len(rows) if max_rows and len(all_rows) > max_rows else 0

    # Calculate column widths
    col_widths = {h: len(h) for h in headers}
    for row in rows:
        for h in headers:
            value = str(row.get(h, ""))
            col_widths[h] = max(col_widths[h], len(value))

    # Parse alignments
    align_map = {}
    if alignments:
        align_list = [a.strip().lower() for a in alignments.split(",")]
        for i, h in enumerate(headers):
            if i < len(align_list):
                align_map[h] = align_list[i]

    # Build header row
    header_line = "| " + " | ".join(h.ljust(col_widths[h]) for h in headers) + " |"

    # Build separator row with alignment
    sep_parts = []
    for h in headers:
        width = col_widths[h]
        align = align_map.get(h, "left")
        if align == "center":
            sep_parts.append(":" + "-" * (width) + ":")
        elif align == "right":
            sep_parts.append("-" * (width + 1) + ":")
        else:
            sep_parts.append("-" * (width + 2))
    separator = "|" + "|".join(sep_parts) + "|"

    # Build data rows
    body_lines = []
    for row in rows:
        cells = []
        for h in headers:
            value = str(row.get(h, ""))
            align = align_map.get(h, "left")
            if align == "right":
                cells.append(value.rjust(col_widths[h]))
            elif align == "center":
                cells.append(value.center(col_widths[h]))
            else:
                cells.append(value.ljust(col_widths[h]))
        body_lines.append("| " + " | ".join(cells) + " |")

    # Combine
    result = "\n".join([header_line, separator] + body_lines)

    if truncated:
        result += f"\n\n*({truncated} more rows not shown)*"

    return result


def main():
    parser = argparse.ArgumentParser(description="Convert CSV to Markdown table")
    parser.add_argument("input", help="Input CSV file path")
    parser.add_argument("--max-rows", type=int, default=None, help="Maximum rows to display")
    parser.add_argument("--columns", type=str, default=None, help="Comma-separated column names to include")
    parser.add_argument("--output", type=str, default=None, help="Output file path (default: stdout)")
    parser.add_argument("--align", type=str, default=None, help="Comma-separated alignments: left, center, right")

    args = parser.parse_args()

    try:
        table = csv_to_markdown(args.input, args.max_rows, args.columns, args.align)
    except FileNotFoundError:
        print(f"Error: File '{args.input}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(table)
        print(f"Table written to {args.output}")
    else:
        print(table)


if __name__ == "__main__":
    main()
