#!/usr/bin/env python3
"""
Keyword & N-gram Analyzer

Reads a text file and outputs word frequency analysis and top n-grams.
Useful for analyzing competitor content, blog posts, and customer feedback.

Usage:
    python analyze-keywords.py input.txt
    python analyze-keywords.py input.txt --top 20
    python analyze-keywords.py input.txt --ngram 3
    python analyze-keywords.py input.txt --output results.md
    python analyze-keywords.py input.txt --min-length 4
    python analyze-keywords.py input.txt --stopwords custom-stopwords.txt
"""

import re
import sys
import argparse
from collections import Counter


# Common English stop words to filter out
DEFAULT_STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "as", "is", "was", "are", "were", "be",
    "been", "being", "have", "has", "had", "do", "does", "did", "will",
    "would", "could", "should", "may", "might", "can", "shall", "not",
    "this", "that", "these", "those", "it", "its", "they", "them", "their",
    "we", "our", "you", "your", "he", "she", "him", "her", "his", "i",
    "me", "my", "mine", "who", "whom", "which", "what", "where", "when",
    "how", "why", "if", "then", "than", "so", "no", "yes", "up", "out",
    "about", "into", "over", "after", "before", "between", "under",
    "again", "further", "once", "here", "there", "all", "each", "every",
    "both", "few", "more", "most", "other", "some", "such", "only", "own",
    "same", "just", "also", "very", "too", "any", "many", "much", "well",
    "still", "even", "now", "new", "one", "two", "first", "last", "get",
    "got", "make", "made", "us", "use", "used", "using", "like",
}


def clean_text(text):
    """Clean and normalize text for analysis."""
    # Remove markdown formatting
    text = re.sub(r"#+\s*", "", text)           # headers
    text = re.sub(r"\*\*|__", "", text)          # bold
    text = re.sub(r"\*|_", "", text)             # italic
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)  # links
    text = re.sub(r"`[^`]+`", "", text)          # inline code
    text = re.sub(r"```[\s\S]*?```", "", text)   # code blocks
    text = re.sub(r"\{\{[^}]+\}\}", "", text)    # template placeholders
    # Remove URLs
    text = re.sub(r"https?://\S+", "", text)
    # Remove special characters but keep hyphens in words
    text = re.sub(r"[^\w\s-]", " ", text)
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)
    return text.lower().strip()


def get_words(text, stop_words, min_length=2):
    """Extract words, filtering stop words and short words."""
    words = text.split()
    return [w for w in words if w not in stop_words and len(w) >= min_length and not w.isdigit()]


def get_ngrams(words, n):
    """Generate n-grams from a list of words."""
    return [" ".join(words[i:i + n]) for i in range(len(words) - n + 1)]


def analyze(input_file, top_n=15, ngram_sizes=None, min_length=2, stop_words=None):
    """Run full analysis on a text file."""
    if ngram_sizes is None:
        ngram_sizes = [2, 3]
    if stop_words is None:
        stop_words = DEFAULT_STOP_WORDS

    with open(input_file, "r", encoding="utf-8") as f:
        raw_text = f.read()

    text = clean_text(raw_text)
    words = get_words(text, stop_words, min_length)

    # Basic stats
    raw_words = raw_text.split()
    total_raw = len(raw_words)
    unique_words = len(set(words))

    lines = []
    lines.append(f"# Keyword Analysis: {input_file}")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total words (raw) | {total_raw:,} |")
    lines.append(f"| Analyzed words (filtered) | {len(words):,} |")
    lines.append(f"| Unique words | {unique_words:,} |")
    lines.append(f"| Vocabulary density | {unique_words / max(len(words), 1) * 100:.1f}% |")
    lines.append("")

    # Word frequency
    word_counts = Counter(words)
    lines.append(f"## Top {top_n} Keywords")
    lines.append("")
    lines.append("| Rank | Word | Count | Frequency |")
    lines.append("|------|------|-------|-----------|")
    for i, (word, count) in enumerate(word_counts.most_common(top_n), 1):
        freq = count / len(words) * 100
        lines.append(f"| {i} | {word} | {count} | {freq:.1f}% |")
    lines.append("")

    # N-grams
    for n in ngram_sizes:
        ngrams = get_ngrams(words, n)
        ngram_counts = Counter(ngrams)
        # Filter n-grams that appear only once
        common_ngrams = [(ng, c) for ng, c in ngram_counts.most_common(top_n * 2) if c > 1][:top_n]

        if common_ngrams:
            lines.append(f"## Top {len(common_ngrams)} {n}-Word Phrases")
            lines.append("")
            lines.append("| Rank | Phrase | Count |")
            lines.append("|------|--------|-------|")
            for i, (ngram, count) in enumerate(common_ngrams, 1):
                lines.append(f"| {i} | {ngram} | {count} |")
            lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Analyze keyword frequency and n-grams in text files")
    parser.add_argument("input", help="Input text or markdown file")
    parser.add_argument("--top", type=int, default=15, help="Number of top results to show (default: 15)")
    parser.add_argument("--ngram", type=int, nargs="+", default=[2, 3], help="N-gram sizes to analyze (default: 2 3)")
    parser.add_argument("--min-length", type=int, default=2, help="Minimum word length (default: 2)")
    parser.add_argument("--output", type=str, default=None, help="Output file (default: stdout)")
    parser.add_argument("--stopwords", type=str, default=None, help="Custom stop words file (one per line)")

    args = parser.parse_args()

    # Load custom stop words if provided
    stop_words = DEFAULT_STOP_WORDS.copy()
    if args.stopwords:
        try:
            with open(args.stopwords, "r") as f:
                custom = {line.strip().lower() for line in f if line.strip()}
            stop_words.update(custom)
        except FileNotFoundError:
            print(f"Warning: Stop words file '{args.stopwords}' not found. Using defaults.")

    try:
        result = analyze(args.input, args.top, args.ngram, args.min_length, stop_words)
    except FileNotFoundError:
        print(f"Error: File '{args.input}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Analysis written to {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
