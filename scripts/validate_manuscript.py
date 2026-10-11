#!/usr/bin/env python3
"""Validate manuscript structure: manifest files exist, figure paths resolve."""
import yaml, os, sys, re, argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--manifest', default='publishing/manuscript.yml')
    p.add_argument('--check-figures', action='store_true')
    args = p.parse_args()
    
    errors = []
    
    # Check manifest exists and all files exist
    if os.path.exists(args.manifest):
        m = yaml.safe_load(open(args.manifest, encoding='utf-8'))
        all_files = []
        all_files.extend(m.get('front_matter', []))
        for part in m.get('parts', []):
            all_files.extend(part.get('files', []))
        all_files.extend(m.get('appendices', []))
        all_files.extend(m.get('back_matter', []))
        all_files.extend(m.get('bibliographies', []))
        
        for f in all_files:
            if not os.path.exists(f):
                errors.append(f'Missing manifest file: {f}')
        print(f'Manifest check: {len(all_files)} files, {len(errors)} missing')
    else:
        print(f'Manifest not found: {args.manifest} (skipping)')
    
    # Check figure paths
    if args.check_figures:
        broken = 0
        total = 0
        for root, dirs, files in os.walk('content'):
            for fn in files:
                if not fn.endswith('.md'): continue
                path = os.path.join(root, fn)
                text = open(path, encoding='utf-8').read()
                for mtch in re.finditer(r'<img src="([^"]+)"', text):
                    total += 1
                    src = mtch.group(1)
                    full = os.path.normpath(os.path.join(root, src))
                    if not os.path.exists(full):
                        errors.append(f'Broken image: {path} -> {src}')
                        broken += 1
                for mtch in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', text):
                    src = mtch.group(1)
                    if src.startswith('http'): continue
                    total += 1
                    full = os.path.normpath(os.path.join(root, src))
                    if not os.path.exists(full):
                        errors.append(f'Broken image: {path} -> {src}')
                        broken += 1
        print(f'Figure check: {total} images, {broken} broken')
    
    if errors:
        print(f'\n{len(errors)} ERRORS:')
        for e in errors[:20]:
            print(f'  {e}')
        sys.exit(1)
    print('\nAll checks passed.')

if __name__ == '__main__':
    main()
