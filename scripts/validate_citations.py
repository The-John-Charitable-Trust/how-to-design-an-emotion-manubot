#!/usr/bin/env python3
"""Validate that all [@key] citations have matching bibliography entries."""
import os, sys, re, json, argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--content-dir', default='content/')
    args = p.parse_args()
    
    # Collect all citation keys used
    used_keys = set()
    for root, dirs, files in os.walk(args.content_dir):
        for fn in files:
            if not fn.endswith('.md'): continue
            text = open(os.path.join(root, fn), encoding='utf-8').read()
            for m in re.finditer(r'\[@([a-zA-Z0-9_]+)', text):
                used_keys.add(m.group(1))
    
    # Collect all defined keys from JSON bibliographies
    defined_keys = set()
    for root, dirs, files in os.walk(os.path.join(args.content_dir, 'references/bibliography')):
        for fn in files:
            if not fn.endswith('.json'): continue
            try:
                entries = json.load(open(os.path.join(root, fn), encoding='utf-8'))
                for e in entries:
                    defined_keys.add(e['id'])
            except:
                pass
    
    # Check for old-style markers
    old_markers = 0
    for root, dirs, files in os.walk(args.content_dir):
        for fn in files:
            if not fn.endswith('.md'): continue
            text = open(os.path.join(root, fn), encoding='utf-8').read()
            old_markers += len(re.findall(r'<sup><a href="[^"]*#note-\d+">', text))
    
    undefined = used_keys - defined_keys
    print(f'Citations used: {len(used_keys)}')
    print(f'Bibliography entries: {len(defined_keys)}')
    print(f'Old-style markers remaining: {old_markers}')
    
    errors = []
    if undefined:
        errors.append(f'{len(undefined)} undefined citation keys: {sorted(undefined)[:10]}')
    if old_markers > 0:
        errors.append(f'{old_markers} old-style markers not converted')
    
    if errors:
        for e in errors:
            print(f'ERROR: {e}')
        sys.exit(1)
    print('All citation checks passed.')

if __name__ == '__main__':
    main()
