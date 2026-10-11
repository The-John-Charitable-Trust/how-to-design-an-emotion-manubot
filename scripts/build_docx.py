#!/usr/bin/env python3
"""
Build DOCX from assembled manuscript markdown using Pandoc.

Usage:
    python scripts/build_docx.py --input build/output/manuscript.md \
        --output build/output/How-To-Design-an-Emotion-Master.docx \
        [--bibliography build/output/bibliography.json] \
        [--csl publishing/chicago-author-date.csl]

Requires: pandoc with citeproc support.
"""

import argparse
import os
import subprocess
import sys


def build_docx(input_path, output_path, bibliography=None, csl=None,
               toc_depth=3):
    if not os.path.exists(input_path):
        print(f'ERROR: Input file not found: {input_path}', file=sys.stderr)
        sys.exit(1)

    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)

    cmd = ['pandoc', input_path, '--citeproc', '-o', output_path]

    if bibliography and os.path.exists(bibliography):
        cmd.extend(['--bibliography', bibliography])
    elif bibliography:
        print(f'WARNING: Bibliography not found: {bibliography}',
              file=sys.stderr)

    if csl and os.path.exists(csl):
        cmd.extend(['--csl', csl])
    elif csl:
        print(f'WARNING: CSL file not found: {csl}', file=sys.stderr)

    cmd.extend(['--toc', f'--toc-depth={toc_depth}'])

    print(f'Running: {" ".join(cmd)}')
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f'ERROR: Pandoc failed:\n{result.stderr}', file=sys.stderr)
        sys.exit(1)

    if result.stderr.strip():
        print(f'Pandoc warnings:\n{result.stderr}', file=sys.stderr)

    size = os.path.getsize(output_path)
    print(f'DOCX built: {output_path} ({size:,} bytes)')


def main():
    parser = argparse.ArgumentParser(
        description='Build DOCX from manuscript markdown via Pandoc')
    parser.add_argument('--input', required=True,
                        help='Input markdown file')
    parser.add_argument('--output', required=True,
                        help='Output DOCX path')
    parser.add_argument('--bibliography', default=None,
                        help='CSL JSON bibliography file')
    parser.add_argument('--csl', default='publishing/chicago-author-date.csl',
                        help='CSL style file')
    parser.add_argument('--toc-depth', type=int, default=3,
                        help='TOC depth (default: 3)')
    args = parser.parse_args()

    build_docx(args.input, args.output, args.bibliography, args.csl,
               args.toc_depth)


if __name__ == '__main__':
    main()
