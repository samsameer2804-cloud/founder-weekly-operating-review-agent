from __future__ import annotations

import argparse
from pathlib import Path

from .analysis import analyze
from .metrics import load_metrics
from .reporting import write_outputs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a founder weekly operating review.")
    parser.add_argument("--metrics", required=True, type=Path, help="Weekly metrics CSV.")
    parser.add_argument("--context", type=Path, help="Company context Markdown file.")
    parser.add_argument("--out", type=Path, default=Path("outputs/demo"), help="Output directory.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    context = args.context.read_text(encoding="utf-8") if args.context else ""
    metrics = load_metrics(args.metrics)
    result = analyze(metrics, context=context)
    write_outputs(result, args.out)
    print(f"Generated weekly operating review in {args.out}")
    return 0
