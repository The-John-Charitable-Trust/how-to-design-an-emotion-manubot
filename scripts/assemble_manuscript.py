#!/usr/bin/env python3
"""
Assemble the manuscript from content files in the order defined by
publishing/manuscript.yml. Outputs a single combined markdown file
ready for Pandoc processing.
"""

import yaml
import os
import sys
import re

def load_manifest(path='publishing/manuscript.yml'):
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)

def read_file(path):
    if not os.path.exists(path):
        print(f'WARNING: Missing file {path}', file=sys.stderr)
        return f'\n\n<!-- MISSING: {path} -->\n\n'
    with open(path, encoding='utf-8') as f:
        content = f.read()
    # Rewrite relative image paths to be relative to repo root
    # Content files use ../../assets/ from content/part-X/, build/ needs assets/
    content_dir = os.path.dirname(path)
    def fix_img(m):
        prefix, src = m.group(1), m.group(2)
        if src.startswith('http'):
            return m.group(0)
        # Resolve relative to content file's directory, then make relative to repo root
        abs_path = os.path.normpath(os.path.join(content_dir, src))
        return f'{prefix}{abs_path}'
    content = re.sub(r'(<img src="|!\[[^\]]*\]\()([^")]+)', fix_img, content)
    return content

def assemble(manifest, output_path='build/manuscript.md'):
    sections = []
    
    # Title block
    sections.append('---')
    sections.append(f'title: "{manifest.get("title", "")}"')
    sections.append(f'author: "{manifest.get("author", "")}"')
    if manifest.get('subtitle'):
        sections.append(f'subtitle: "{manifest["subtitle"]}"')
    sections.append('---')
    sections.append('')
    
    # Front matter
    for f in manifest.get('front_matter', []):
        content = read_file(f)
        # Mark section breakers for styling
        if 'related-books' in f or f.endswith('introduction.md'):
            content = '<div class="section-breaker">\n\n' + content + '\n\n</div>'
        sections.append(content)
        sections.append('\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n')
    
    # Parts
    for part in manifest.get('parts', []):
        for f in part.get('files', []):
            content = read_file(f)
            if '_part.md' in f:
                # Style as navy section breaker
                content = '<div class="section-breaker part-divider">\n\n' + content + '\n\n</div>'
            elif '_metamorphosis.md' in f:
                content = '<div class="section-breaker metamorphosis">\n\n' + content + '\n\n</div>'
            sections.append(content)
            sections.append('\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n')
    
    # Appendices
    for f in manifest.get('appendices', []):
        sections.append(read_file(f))
        sections.append('\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n')
    
    # Back matter
    for f in manifest.get('back_matter', []):
        sections.append(read_file(f))
        sections.append('\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n')
    
    # Combine bibliography JSON files
    import json
    all_entries = []
    seen_ids = set()
    for bf in manifest.get('bibliographies', []):
        if os.path.exists(bf):
            entries = json.load(open(bf, encoding='utf-8'))
            for e in entries:
                if e['id'] not in seen_ids:
                    seen_ids.add(e['id'])
                    all_entries.append(e)
    
    # Write combined bibliography
    os.makedirs('build', exist_ok=True)
    json.dump(all_entries, open('build/bibliography.json', 'w'), indent=2)
    print(f'Combined {len(all_entries)} bibliography entries')
    
    # Write assembled manuscript
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sections))
    print(f'Manuscript assembled: {output_path} ({len(sections)} sections)')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Assemble manuscript from manifest')
    parser.add_argument('--manifest', default='publishing/manuscript.yml',
                        help='Path to manuscript manifest YAML')
    parser.add_argument('--output', default='build/manuscript.md',
                        help='Output path for assembled markdown')
    # Backwards compat: positional arg as output path
    parser.add_argument('positional_output', nargs='?',
                        help='Output path (positional, deprecated)')
    args = parser.parse_args()

    output = args.output
    if args.positional_output and args.output == 'build/manuscript.md':
        output = args.positional_output

    manifest = load_manifest(args.manifest)
    assemble(manifest, output)
