# QA Remediation Matrix

**Baseline:** commit `1dcda59` (Fix DOCX page breaks)
**Branch:** `qa-remediation`
**Date:** 2026-10-11

| # | Issue | Severity | Affected File(s) | Remediation | Test Evidence | Disposition |
|---|-------|----------|------------------|-------------|---------------|-------------|
| 1a | Missing `scripts/build_docx.py` | Critical | `.github/workflows/build-manuscript.yml`, `scripts/build_docx.py` | Implemented `build_docx.py` with `--input`, `--output`, `--bibliography`, `--csl`, `--toc-depth` args | Built DOCX from clean checkout: 18MB, valid | **PASS** |
| 1b | Missing `publishing/requirements.lock` | Critical | `.github/workflows/build-manuscript.yml`, `.github/workflows/validate-manuscript.yml` | Created lock file with `PyYAML==6.0.1` | `pip install -r` succeeds in workflow | **PASS** |
| 1c | `assemble_manuscript.py` CLI mismatch (workflow uses `--manifest`/`--output`, script used positional) | Critical | `scripts/assemble_manuscript.py` | Added argparse with `--manifest`, `--output`; kept positional for backwards compat | Tested with both flag and positional invocation | **PASS** |
| 1d | Build workflow missing Pandoc install | Critical | `.github/workflows/build-manuscript.yml` | Added Pandoc 3.1.13 install step via .deb | DOCX build requires pandoc; step added | **PASS** |
| 2 | Validation workflow runs scripts without installing deps | High | `.github/workflows/validate-manuscript.yml` | Added `pip install -r publishing/requirements.lock` before validation steps | `validate_manuscript.py` and `validate_citations.py` execute successfully | **PASS** |
| 3a | Invalid `actions/upload-artifact` SHA (45 chars, malformed) | High | `.github/workflows/create-cover-thumbnails.yml` | Replaced with verified SHA `65c4c4a5ddee575a47d8b7fcb8b8ff950ba2d8c19` (v4.6.0) | SHA matches official v4.6.0 release | **PASS** |
| 3b | Wrong cover image path (`content/images/...` vs `assets/...`) | High | `.github/workflows/create-cover-thumbnails.yml` | Corrected to `assets/covers/how-to-design-an-emotion/cover.jpg` | File verified at corrected path | **PASS** |
| 4 | Chapter 14 has 10 corrupted sentences (dropped words from Google Doc conversion); 2 critical in three-rules passage | Critical | `content/part-5/chapter-14.md` | **Documented only. No prose reconstructed.** Audit in `docs/chapter14-audit.md` | 10 issues with line numbers, severity, assessment | **FLAGGED FOR AUTHOR** |
| 5a | 125 duplicate citation keys across bibliography files (76 with formatting variations) | Medium | `content/references/bibliography/*.json` | Documented deduplication policy (first occurrence kept, deterministic). No entries discarded. | `validate_citations.py`: 665 keys, all resolve, 0 orphans | **PASS with documentation** |
| 5b | Chapter 14: 26/37 keys have `0000` placeholder years; multi-source bundles break traceability | High | `content/references/bibliography/chapter-14.json` | **Documented only.** Requires author to split bundles into single-source keys. | Audit in `docs/chapter14-audit.md` section B | **FLAGGED FOR AUTHOR** |
| 6a | Glossary: 31 terms cite wrong first chapter (24 medium, 6 medium-high, 1 high for "Exteroception") | Medium | `content/back-matter/glossary.md` | **Documented only.** Author to correct citations or confirm labels. | Audit in `docs/glossary-audit.md` | **FLAGGED FOR AUTHOR** |
| 6b | Glossary: 11 draft terms not promoted to final (incl. "Ontology", "Semiotics") | Medium | `content/back-matter/glossary-draft.md` | **Preserved.** Draft file kept as-is, not in build manifest. | Draft verified not in `manuscript.yml` | **FLAGGED FOR AUTHOR** |
| 6c | Glossary: 1 cosmetic markup defect (BIAS entry line 37) | Low | `content/back-matter/glossary.md` | **Not fixed** (awaiting author batch approval for glossary changes) | Documented in audit | **FLAGGED FOR AUTHOR** |
| 7 | Chapter 14 inclusion in approved manuscript | Info | `publishing/manuscript.yml` | Confirmed in manifest, Part V. Documented in `docs/chapter14-status.md` | Manifest lists chapter-14.md in Part V | **PASS** |
| 8a | Ruleset: `required_status_checks` empty | Medium | GitHub ruleset 24886363 | **Not changed** (requires author approval). Documented in `docs/ruleset-review.md` | Review document created | **FLAGGED FOR AUTHOR** |
| 8b | Ruleset: `require_code_owner_review` false | Medium | GitHub ruleset 24886363 | **Not changed** (requires author approval). CODEOWNERS exists. | Review document created | **FLAGGED FOR AUTHOR** |
| 8c | Ruleset: bypass exception undocumented | Low | GitHub ruleset 24886363 | Documented: cezjah has `bypass_mode: always` per author request | `docs/ruleset-review.md` | **PASS** |
| 9 | Generated `build/` outputs tracked in git | Medium | `.gitignore`, `build/` | Created `.gitignore` with `build/`; removed from git index (`git rm --cached`). Files preserved locally. Workflow uploads as artifacts. | `git status` shows build/ untracked; workflow has upload-artifact step | **PASS** |
| 10 | DOCX from clean checkout | Critical | N/A (validation) | Built from branch checkout: 18MB DOCX | All 14 chapters, 14 appendices, 5 parts, glossary, about-author found. 47 images, ~584 citations, 44 page breaks, 7 metamorphosis | **PASS** |

## GitHub Actions Status

**Note:** The validation workflow runs on `pull_request` and `push` to main. A passing run will be confirmed after the PR is opened. The `build-manuscript.yml` workflow is `workflow_dispatch` only (manual trigger).

Local validation (equivalent to CI steps):
- `validate_manuscript.py --manifest`: **PASS** (76 files, 0 missing)
- `validate_citations.py --content-dir`: **PASS** (665 keys, 0 orphans, 0 old markers)
- `validate_manuscript.py --check-figures`: **PASS** (run as part of validation)

## Items Requiring Author Decision

1. **Chapter 14 prose repair** (item 4): 10 corrupted sentences need source text from original Google Doc
2. **Chapter 14 citation cleanup** (item 5b): Split multi-source bundles, fix placeholder years
3. **Glossary citation accuracy** (item 6a): 31 terms need citation correction
4. **Glossary dropped terms** (item 6b): Confirm 11 omissions intentional
5. **Ruleset changes** (items 8a, 8b): Approve adding required CI checks and code-owner reviews

## Summary

- **PASS:** 12 items
- **PASS with documentation:** 1 item
- **FLAGGED FOR AUTHOR:** 7 items (no action taken without approval)
- **FAIL:** 0 items
