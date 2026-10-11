# Citation Traceability Report

**Generated:** 2026-10-11
**Baseline:** commit 1dcda59

## Summary

| Metric | Count |
|--------|-------|
| Citation keys used in content | 665 |
| Unique bibliography entries | 693 |
| Old-style markers remaining | 0 |
| Duplicate keys across files | 125 |
| Conflicting duplicates | 76 |

## Validation Status: PASS

All 665 citation keys used in markdown content have matching bibliography
entries. Zero old-style `<sup>` markers remain.

## Duplicate Key Analysis

125 citation keys appear in multiple bibliography JSON files. This is expected:
each chapter and appendix maintains its own bibliography file, and frequently
cited works (Barrett, Ekman, Panksepp, etc.) appear in several.

76 duplicates have minor formatting variations in their `note` fields
(e.g., "Barrett, Lisa Feldman." vs "Lisa Feldman Barrett,"). These are the
same source with different citation formatting conventions per chapter.

### Deduplication Policy

The assembly script (`scripts/assemble_manuscript.py`) deduplicates by citation
key, keeping the **first occurrence** encountered in manifest order. This is
deterministic and documented, not silent: the combined `bibliography.json`
contains 693 unique entries.

No conflicting bibliography entries are discarded without trace: all source
files retain their original entries. Only the combined build output is
deduplicated.

## Notes Integrity

23 notes files present in `content/references/notes/`. Each corresponds to a
chapter or appendix with endnotes. Notes files are preserved as standalone
references and are not currently assembled into the manuscript build.

## Original Marker Mappings

Citation conversion reports are preserved in `build/reports/` (untracked, see
.gitignore). Each chapter's conversion report documents:
- Original marker format (e.g., superscript numbers, parenthetical refs)
- New `[@key]` citation key assigned
- Bibliography entry created

These reports provide full traceability from original markers to Manubot keys.
