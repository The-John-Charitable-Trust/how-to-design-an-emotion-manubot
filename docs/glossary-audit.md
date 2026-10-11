# Glossary Audit Report

**Repository:** `The-John-Charitable-Trust/how-to-design-an-emotion-manubot`
**Branch:** `qa-remediation`
**Baseline commit:** `1dcda5994e10ccf43479c64ed85d3375107d6e37`
**File audited:** `content/back-matter/glossary.md` (259 lines)
**Draft compared:** `content/back-matter/glossary-draft.md` (115 lines)
**Audit date:** 2026-10-11
**Method:** Automated parsing + full-text search across all `content/**/*.md` files (excluding glossary files themselves). No files modified.

---

## Summary

| Metric | Result |
|---|---|
| Total terms in `glossary.md` | **109** |
| Terms missing definitions | **0** |
| Terms with placeholder markers (`[DEFINITION NEEDED]`, TBD, TODO) | **0** |
| Terms with no chapter citations | **0** |
| Terms with malformed citations (bad chapter/appendix refs) | **0** |
| Terms with formatting defects | **1** |
| Terms whose first-cited chapter does not contain the term | **31** |
| Terms with zero presence in manuscript (exact phrase) | **7** |
| Terms with zero presence even as component words | **1** |

**Overall severity: MEDIUM.** The glossary is structurally complete (all terms defined, all cited, no placeholders). The primary issue is citation accuracy: 28% of terms cite a chapter first where the term does not appear, and one term ("Exteroception") has no traceable presence in the manuscript at all.

---

## 1. Terms Missing Definitions

**None.** All 109 terms have substantive definitions (minimum body length well above threshold after stripping citations and cross-references).

**Severity:** N/A — PASS

---

## 2. Terms with Broken/Missing Chapter Citations

**No structurally broken citations.** Every term carries at least one citation in the format `[Chapter N, Title; Appendix X, Title]`, and all chapter/appendix numbers reference real sections of the manuscript. All cited titles match the actual chapter/appendix titles.

However, **31 terms (28%) cite a chapter first where the exact term phrase does not appear** in that chapter. These fall into three sub-categories:

### 2a. Terms absent from cited chapter but present elsewhere (24 terms) — SEVERITY: MEDIUM

The citation points to the wrong primary location. The term is real and used in the manuscript, but the first-listed citation is inaccurate.

| Term | First cited | Actually appears in |
|---|---|---|
| Affective character | Chapter 1 | methodology.md, Chapter 9, Chapter 10 |
| Affective timbre | Chapter 13 | introduction.md, methodology.md |
| Binding | Chapter 7 | Appendix A, J, K (not in Ch 7 at all) |
| Conceptual constraint | Chapter 2 | Appendix J, M, N |
| Emotion category | Chapter 13 | Appendix A, notes/bibliography files |
| Emotionese | Chapter 11 | Appendix L, Chapter 10, Chapter 12 |
| Enculturation | Chapter 11 | Appendix M |
| Goal-governed constraint | Chapter 6 | introduction.md, Chapter 7, Chapter 12 |
| Indicator | Chapter 12 | Appendix A |
| Interpretive error | Chapter 12 | Appendix K, introduction.md |
| Lexical concept | Chapter 10 | Chapter 2, Chapter 5 |
| Macro-semiotic architecture | Chapter 7 | Chapter 8, Chapter 9 |
| Metamorphosis of an ontology | Chapter 14 | part-1/2/3 `_metamorphosis.md` files |
| Micro-semiotic constituents | Chapter 10 | Chapter 9 |
| Misattribution of affect | Chapter 12 | methodology.md |
| Misinstantiation | Chapter 4 | Appendix E |
| Natural kind | Chapter 12 | Appendix A, B, F |
| Operational identity | Chapter 4 | Chapter 5 |
| Phenomenological experience | Chapter 1 | Appendix L, methodology.md, Chapter 9 |
| Referent-in-context | Chapter 9 | Appendix M, Chapter 10 |
| Semiotic availability | Chapter 7 | methodology.md, Chapter 9, Chapter 10 |
| Sign-material | Chapter 7 | Chapter 9 (zero occurrences in Ch 7) |
| Structural revision | Chapter 9 | Appendix E |
| Weighted score matrix trade study | Appendix I | Chapter 9 |

**Notable cases:**
- **"Binding"** cites Chapter 7 first but the word "binding" appears zero times in Chapter 7. It is used in Appendices A, J, K.
- **"Sign-material"** cites Chapter 7 first but has zero occurrences in Chapter 7. It appears in Chapter 9.
- **"Metamorphosis of an ontology"** cites Chapter 14 first, but the phrase primarily lives in the `_metamorphosis.md` closing pages of Parts 1-3.

### 2b. Terms with no exact-phrase match anywhere in manuscript (7 terms) — SEVERITY: MEDIUM-HIGH

These terms do not appear as exact phrases in any content file. Their component words appear together in related passages, suggesting the glossary uses a compound label for a concept discussed under different wording.

| Term | First cited | Component words found together in |
|---|---|---|
| Appraisal constraint | Appendix K | Appendix A, B, F, K; introduction.md |
| Emotional prototype | Chapter 12 | Appendix A, B, L; introduction.md; methodology.md |
| Emotional stereotype | Chapter 12 | Appendix L; methodology.md; Chapter 12, 14 |
| First-person emotional reality | Chapter 12 | introduction.md; methodology.md; preface.md; Ch 1, 8 |
| Objective reality | Chapter 12 | introduction.md; preface.md; Ch 1, 2, 8 |
| Social emotional reality | Chapter 12 | introduction.md; methodology.md; preface.md; Ch 1, 8 |
| **Exteroception** | **Chapter 9** | **NOWHERE — not even component words** |

**"Exteroception" is the most severe case.** It is cited to Chapter 9, but neither the term nor its component words appear together in any manuscript file. This term cannot be traced to any cited passage.

### 2c. Recommended remediation (not applied — documentation only)

Per the QA brief: do not silently discard entries. For each of the 31 terms above, the author should either (a) correct the first-cited chapter to where the term actually receives primary treatment, or (b) confirm the glossary's compound label is the authoritative name for a concept discussed under different wording in the cited chapter.

---

## 3. Formatting Defects

**One malformed entry:**

- **Line 37:** `**Biological Intelligence Application Server****(BIAS)**.`
  The parenthetical acronym is wrapped in a separate bold span (`****(BIAS)**`), producing broken Markdown rendering. Should be `**Biological Intelligence Application Server (BIAS)**.`
  
  **Severity:** LOW (cosmetic, does not affect content)

All other 108 terms follow the `**Term**. Definition... [citations]` format consistently. Section headers (A, B, C, D, E, F, G, I, L, M, N, O, P, R, S, T, V, W) are present and terms are alphabetically sorted within sections.

---

## 4. Draft vs Final Comparison

`content/back-matter/glossary-draft.md` exists (115 lines, 24 terms). Its header states: *"Draft - extracted from manuscript text. Definitions require author review and approval."*

### 4a. Draft quality issues (for context — draft is superseded, not in build)

The draft contains **13 terms marked `[DEFINITION NEEDED - to be supplied by author]`** and several entries with fragment definitions that appear to be sentence fragments scraped from manuscript text rather than definitions:

| Draft term | Draft state |
|---|---|
| Affect | `[DEFINITION NEEDED]` |
| Agent | Fragment: "not a temporary hurdle for technology to clear." |
| Allostasis | `[DEFINITION NEEDED]` |
| Architecture | Fragment: "the constant; developmental timing may vary across individuals." |
| Arousal | `[DEFINITION NEEDED]` |
| Category | Fragment: "the set of all objects that instantiate a class." |
| Commitment | `[DEFINITION NEEDED]` |
| Concept | Fragment: "to grasp the necessary and sufficient conditions..." |
| Constraint | `[DEFINITION NEEDED]` |
| Construct | Fragment: "the extensional realization of a concept." |
| Core affect | `[DEFINITION NEEDED]` |
| Emotion | `[DEFINITION NEEDED]` |
| Essence | `[DEFINITION NEEDED]` |
| Feeling | Fragment: "not identical to bodily sensation itself..." |
| Identity | `[DEFINITION NEEDED]` |
| Interoception | `[DEFINITION NEEDED]` |
| Interpretation | `[DEFINITION NEEDED]` |
| Meaning | `[DEFINITION NEEDED]` |
| Ontology | `[DEFINITION NEEDED]` |
| Referent | Fragment: "the situated object of interpretation." |
| Semiotics | `[DEFINITION NEEDED]` |
| Sign | Fragment: "interpreted relative to a goal..." |
| Symbol | `[DEFINITION NEEDED]` |
| Valence | `[DEFINITION NEEDED]` |

### 4b. Promotion status

- **13 of 24 draft terms** were promoted to the final glossary with full definitions and proper citations: Affect, Agent, Category, Concept, Construct, Emotion, Feeling, Interoception, Interpretation, Meaning, Referent, Symbol, Valence.
- **11 of 24 draft terms** were **not carried into the final glossary**: Allostasis, Architecture, Arousal, Commitment, Constraint, Core affect, Essence, Identity, Ontology, Semiotics, Sign.

**Per the QA brief, these 11 dropped terms are documented here and NOT deleted.** The draft file is preserved as-is. Disposition of the 11 dropped terms (whether intentionally cut or accidentally omitted) requires author decision:
- "Ontology", "Identity", "Essence", "Semiotics", "Sign", and "Architecture" are notable omissions given their centrality to the book's subject matter.
- "Allostasis", "Arousal", "Core affect" are key emotion-science terms that may have been folded into other entries (e.g., "Affect", "Physiological affect").

### 4c. Draft inclusion in build

The draft file (`glossary-draft.md`) is **not** referenced in `publishing/manuscript.yml` (verified: only `glossary.md` is in the assembly manifest). It does not appear in any built output. No action needed, but it should remain preserved per the QA brief.

**Severity:** LOW for the draft itself (superseded, not in build). The 11 dropped terms are flagged as **MEDIUM** pending author confirmation that omission was intentional.

---

## 5. Severity Assessment Summary

| # | Issue | Severity | Count | Disposition |
|---|---|---|---|---|
| 1 | Terms missing definitions | — | 0 | PASS |
| 2 | Placeholder/draft markers in final glossary | — | 0 | PASS |
| 3 | Terms with no citations | — | 0 | PASS |
| 4 | Structurally invalid citations | — | 0 | PASS |
| 5 | First-cited chapter does not contain term (term exists elsewhere) | MEDIUM | 24 | Author review: correct citation or confirm label |
| 6 | Term has no exact-phrase match in manuscript | MEDIUM-HIGH | 6 | Author review: confirm glossary label vs manuscript wording |
| 7 | "Exteroception" — untraceable to any manuscript passage | HIGH | 1 | Author decision: supply source passage or remove term |
| 8 | Malformed bold markup on BIAS entry (line 37) | LOW | 1 | Mechanical fix, safe to apply |
| 9 | 11 draft terms not promoted to final glossary | MEDIUM | 11 | Author decision: intentional cut or accidental omission |
| 10 | Draft file contains placeholder fragments | LOW | — | Preserved as-is per QA brief; not in build |

---

## 6. Test Evidence

- Parsed all 109 glossary entries with regex; verified each has a definition body (>20 chars after stripping citations), at least one `[Chapter/Appendix]` citation, and no placeholder markers.
- Validated all cited chapter/appendix numbers and titles against the manuscript structure (Chapters 1-14, Appendices A-N, Introduction, Preface).
- Full-text searched every `content/**/*.md` file (excluding glossary files) for each term as exact phrase, hyphen/space variants, and component-word co-occurrence.
- Compared draft (24 terms) against final (109 terms) by normalized term name.
- Verified `glossary-draft.md` is not in `publishing/manuscript.yml` assembly manifest.
- **No files were created, modified, or deleted during this audit.**

---

## Verdict

**CONDITIONAL PASS.** The glossary is complete and well-formed as a document: 109 defined terms, full citations, no placeholders, consistent formatting (one cosmetic markup defect). It is suitable for inclusion in the build.

**Before final acceptance, the author should review:**
1. The 31 citation-accuracy flags (Section 2) — particularly "Exteroception" (untraceable) and the "Binding"/"Sign-material" wrong-chapter citations.
2. The 11 draft terms omitted from the final glossary (Section 4b) — confirm intentional.
3. The one-line markup fix on the BIAS entry (line 37).
