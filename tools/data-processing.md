# Data Processing Guide

> How to use Claude Code's bash and Python capabilities to process CSV, JSON, and markdown data.

---

## Available Capabilities

Claude Code can run bash commands and Python scripts directly. No package installation needed for standard library modules. Use these for data manipulation, calculations, and report generation.

---

## CSV Operations

### Read a CSV and Display as Markdown Table

Use the helper script:
```bash
python tools/scripts/csv-to-table.py input.csv
```

### Quick CSV Stats with Python

```python
import csv
import sys
from collections import Counter

with open(sys.argv[1], 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Total rows: {len(rows)}")
print(f"Columns: {', '.join(rows[0].keys())}")

# Count values in a specific column
col = sys.argv[2] if len(sys.argv) > 2 else list(rows[0].keys())[0]
counts = Counter(row[col] for row in rows)
print(f"\nTop values in '{col}':")
for value, count in counts.most_common(10):
    print(f"  {value}: {count}")
```

### Filter CSV Rows

```python
import csv
import sys

input_file = sys.argv[1]
column = sys.argv[2]
value = sys.argv[3]
output_file = sys.argv[4] if len(sys.argv) > 4 else 'filtered.csv'

with open(input_file, 'r') as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader if value.lower() in row.get(column, '').lower()]

if rows:
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Filtered {len(rows)} rows where '{column}' contains '{value}'")
else:
    print("No matching rows found")
```

### Sort CSV

```python
import csv
import sys

input_file = sys.argv[1]
sort_column = sys.argv[2]
reverse = '--desc' in sys.argv

with open(input_file, 'r') as f:
    reader = csv.DictReader(f)
    rows = sorted(list(reader), key=lambda x: x.get(sort_column, ''), reverse=reverse)

with open(input_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Sorted by '{sort_column}' {'descending' if reverse else 'ascending'}")
```

---

## JSON Operations

### Pretty-Print JSON

```bash
python -m json.tool input.json
```

### Extract Fields from JSON

```python
import json
import sys

with open(sys.argv[1], 'r') as f:
    data = json.load(f)

# If it's a list of objects, extract specific fields
if isinstance(data, list):
    fields = sys.argv[2:]  # field names as arguments
    for item in data:
        values = [str(item.get(f, 'N/A')) for f in fields]
        print(' | '.join(values))
```

### Convert JSON to CSV

```python
import json
import csv
import sys

with open(sys.argv[1], 'r') as f:
    data = json.load(f)

if isinstance(data, list) and data:
    output = sys.argv[2] if len(sys.argv) > 2 else 'output.csv'
    with open(output, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Converted {len(data)} records to {output}")
```

### Convert CSV to JSON

```python
import json
import csv
import sys

with open(sys.argv[1], 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

output = sys.argv[2] if len(sys.argv) > 2 else 'output.json'
with open(output, 'w') as f:
    json.dump(data, f, indent=2)
print(f"Converted {len(data)} rows to {output}")
```

---

## Markdown Table Generation

### From Inline Data

```python
def make_table(headers, rows):
    """Generate a markdown table from headers and row data."""
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    header_line = '| ' + ' | '.join(h.ljust(col_widths[i]) for i, h in enumerate(headers)) + ' |'
    separator = '|' + '|'.join('-' * (w + 2) for w in col_widths) + '|'
    body_lines = []
    for row in rows:
        body_lines.append('| ' + ' | '.join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)) + ' |')

    return '\n'.join([header_line, separator] + body_lines)
```

### From CSV File to Markdown

Use the helper script:
```bash
python tools/scripts/csv-to-table.py data.csv
```

---

## Calculations

### ROI Calculator

```python
def calculate_roi(hours_saved, hourly_rate=150):
    """Calculate ROI for agency work."""
    value = hours_saved * hourly_rate
    print(f"Hours of work: {hours_saved}")
    print(f"Industry rate: ${hourly_rate}/hr")
    print(f"Value delivered: ${value:,.2f}")
    return value

# Example usage
deliverables = {
    'Blog posts': (4, 3),      # (count, hours_each)
    'Social posts': (30, 0.5),
    'Email sequence': (5, 1.5),
    'Strategy doc': (1, 8),
    'Research report': (1, 6),
}

total_hours = 0
for item, (count, hours) in deliverables.items():
    item_hours = count * hours
    total_hours += item_hours
    print(f"{item}: {count} x {hours}h = {item_hours}h (${item_hours * 150:,.2f})")

print(f"\nTotal: {total_hours}h = ${total_hours * 150:,.2f}")
```

### Campaign Metrics

```python
def campaign_metrics(impressions, clicks, conversions, cost=0):
    """Calculate key campaign metrics."""
    ctr = (clicks / impressions * 100) if impressions else 0
    conv_rate = (conversions / clicks * 100) if clicks else 0
    cpc = (cost / clicks) if clicks else 0
    cpa = (cost / conversions) if conversions else 0

    print(f"Impressions: {impressions:,}")
    print(f"Clicks: {clicks:,}")
    print(f"CTR: {ctr:.2f}%")
    print(f"Conversions: {conversions:,}")
    print(f"Conv. Rate: {conv_rate:.2f}%")
    if cost:
        print(f"Cost: ${cost:,.2f}")
        print(f"CPC: ${cpc:.2f}")
        print(f"CPA: ${cpa:.2f}")
```

---

## Text Analysis

### Word Frequency

Use the helper script:
```bash
python tools/scripts/analyze-keywords.py input.txt
```

### Content Length Check

```python
import sys

with open(sys.argv[1], 'r') as f:
    text = f.read()

words = text.split()
sentences = text.count('.') + text.count('!') + text.count('?')
paragraphs = text.count('\n\n') + 1

print(f"Words: {len(words)}")
print(f"Sentences: {sentences}")
print(f"Paragraphs: {paragraphs}")
print(f"Avg words/sentence: {len(words)/max(sentences,1):.1f}")
print(f"Reading time: ~{len(words)//200} min")
```

---

## File Operations

### Combine Multiple Markdown Files

```bash
# Combine all markdown files in a directory
cat output/client/2025-01-15/*.md > output/client/2025-01-15/combined-report.md
```

### Count Deliverables

```bash
# Count files by type in output directory
find output/ -name "*.md" | wc -l
find output/ -name "*.csv" | wc -l
```

### Generate Directory Listing

```bash
# List all deliverables for a client
find output/[client]/ -type f -name "*.md" | sort
```

---

## Tips

- **Always save intermediate data** — Write CSVs and JSONs to vault for reuse
- **Use markdown tables in deliverables** — They render well in Obsidian and everywhere else
- **Chain operations** — Pipe commands together for multi-step processing
- **Back up before transforming** — Copy files before running destructive operations
- **Use the helper scripts** — They're in `tools/scripts/` and handle common tasks
