# Chapter 14 Audit — Incomplete / Corrupted Sentences

**File:** `content/part-5/chapter-14.md`
**Branch:** `qa-remediation` (baseline commit `1dcda59`)
**Bibliography:** `content/references/bibliography/chapter-14.json` (37 entries)
**Date:** 2026-10-11
**Method:** Full read of all 81 lines; double-space scan for dropped words; citation-key cross-check against the JSON bibliography. No prose was rewritten.

**Limitation:** The authoritative source (the original Google Doc) was not available to this audit, so "corruption" is assessed from internal evidence only: grammar breaks, double/triple spaces marking dropped words, and comparison with intact parallel passages in the same chapter.

---

## A. Prose issues

### 1. Line 7 — Duplicate heading (minor)
> "So What Is an Emotion?: A Unified Ontology of Affect, Feeling, and Emotion"

Repeats the H1 title (line 3) and the italic subtitle (line 5) verbatim as plain body text. Likely a Google Doc title block carried into the body during conversion.
**Assessment:** Corruption (conversion artifact), not intentional style.

### 2. Line 11 — Missing verb (major)
> "I have answered those questions by  a clear architecture: external events initiate conditions..."

Double space after "by" marks a dropped word (e.g. "constructing", "building"). The sentence is ungrammatical as written.
**Assessment:** Corruption.

### 3. Line 13 — Missing clause (major)
> "This framework also clarifies  Non-human animals display attraction, aversion, and distress before reflective judgment."

"Clarifies" has no object; the sentence jumps to a new thought. A clause was dropped at the double space (the framework clarifies *something*, presumably whether animal affect counts as emotion).
**Assessment:** Corruption.

### 4. Line 19 — Missing object (major)
> "Only after that progression could I identify  more precisely as feeling: the conscious metaperceptual awareness..."

Missing direct object after "identify" (e.g. "it", "experience", "phenomenological experience").
**Assessment:** Corruption.

### 5. Line 25 — Missing noun (major)
> "I define affect as the physiological and regulatory  that generates the conditions of feeling without itself constituting feeling or emotion."

Missing noun after "regulatory" (e.g. "processes", "states", "systems"). This is a formal definition, so the gap is load-bearing.
**Assessment:** Corruption.

### 6. Line 29 — Two missing words (major)
> "I define emotion as a goal-governed, context-sensitive semiotic interpretive through which agents assign meaning to feeling by organizing  timbre into emotion categories..."

Two gaps: (a) missing noun after "interpretive" — line 21 in the same chapter gives the intact parallel phrase "a semiotic interpretive **act** through which an agent assigns meaning"; (b) missing adjective before "timbre" — likely "phenomenological", the book's standard term.
**Assessment:** Corruption. The parallel passage on line 21 confirms what was lost.

### 7. Line 41 — Fused sentences (major)
> "By bringing these disciplines into one constrained architecture The result is not an eclectic collection of perspectives, but a division of explanatory labor..."

Two sentences fused with no punctuation between "architecture" and "The". A period (or comma + conjunction) was dropped.
**Assessment:** Corruption.

### 8. Line 61 — Dropped leading text (critical)
> "First,  omponent with the whole."

Chapter 1's first rule is "do not confuse a component with the whole". The text lost "Do not confuse a c" — only "omponent with the whole." survives. This is the book's thesis restated in its conclusion.
**Assessment:** Corruption. Critical because it damages the restatement of the book's central rule.

### 9. Line 63 — Dropped text in two places (critical)
> "Second,   with essence. Physiological signals, facial expressions, behavior, verbal reports, and felt states may provide evidence of emotion, but   to establish  identity conditions."

Triple space after "Second," marks the loss of "Do not confuse evidence" (the second rule). Later, "but   to establish  identity conditions" lost its verb phrase (probably "they are insufficient to establish the identity conditions" or similar). The sentence is ungrammatical and the rule itself is unstatable from this text.
**Assessment:** Corruption. Critical — same reason as #8.

### 10. Line 65 — Partially intact rule (major)
> "Third, naming with knowing."

The full rule is "do not confuse naming with knowing". The verb phrase is missing here too, though the noun phrase survived intact — inconsistent with lines 61/63 where even the noun phrases were damaged.
**Assessment:** Corruption (partial). The pattern across lines 61-65 suggests the phrase "do not confuse" (and surrounding words) was systematically stripped in this passage, possibly an artifact of tracked-change or comment handling in the Google Doc conversion.

---

## B. Citation traceability

**Key coverage: PASS.** All 37 `[@key]` markers used in the chapter resolve to entries in `chapter-14.json`. Zero unmatched keys; zero unused entries.

**Traceability quality: FAIL (major/critical issues below).**

### 11. Placeholder years in 70% of keys (major)
26 of 37 citation keys contain `0000` as the year (e.g. `[@lazarus0000appraisal]`, `[@damasio0000how]`, `[@barrett0000work]`, `[@peirce0000ad]`, `[@gupta0000definitions]`). These are auto-generated placeholder keys, not stable scholarly identifiers. 10 entries lack an author field and 26 lack a year field in the JSON.

### 12. Multi-source bundles break 1:1 traceability (critical)
Nearly every note in `chapter-14.json` contains **multiple works separated by semicolons**. Examples:
- `damasio0000how`: "Damasio, The Feeling of What Happens; Craig, 'How Do You Feel?'; Barrett, How Emotions Are Made..."
- `lazarus0000appraisal`: "Lazarus, Emotion and Adaptation; Scherer, 'Appraisal Considered as a Process of Multilevel Sequential Checking'; Ira J. ..."
- `barrett0000work`: "Barrett, How Emotions Are Made; Searle, The Construction of Social Reality; Damasio, The Feeling of What Happens; Peirce..."

A single `[@key]` marker therefore cites 3-5 sources at once. There is no way to determine which source supports which claim. This also corrupted the CSL enrichment pass: `barrett0000work` now has author `{family: "Barrett", given: "How"}` (parsed from "Barrett, How Emotions Are Made"), `peirce0000ad` has `{family: "Peirce", given: "The"}`. These structured fields are wrong and will render incorrect citations.

### 13. Near-duplicate numbered keys (major)
Numbered suffix variants (`damasio0000how` through `damasio0000how5`, `barrett0000are`/`are2`/`are3`, `brandom0000work`/`work2`/`work3`, `marr0000work`/`work2`, `frege0000on`/`on2`) share heavily overlapping note text — they are near-duplicate bundles created to disambiguate citation points, not distinct sources. E.g. `damasio0000how` and `damasio0000how2` share identical first-80 characters and differ only in trailing works. These should be deduplicated or split into single-source keys, not silently merged.

### 14. Key-naming anomalies (minor)
- `group0000work` — "group" derives from "Object Management Group" (an organization author); the key is misleading.
- Suffixes derived from title words rather than clean identifiers: `what` (`james2004what`, `james1962what`), `are` (`marr0000are`, `barrett0000are`), `how`, `on`, `work`, `ad` (`peirce0000ad`).

---

## C. Clean checks

- **No encoding issues:** no replacement characters (U+FFFD), no mojibake. Only non-ASCII characters are the intentional `·` separators (line 1) and the em dash (line 3).
- **No placeholder markers:** no TODO, FIXME, XXX, `[missing]`, `[insert]`, or lorem ipsum.
- **Logical flow intact:** where sentences are complete, the chapter reads as a coherent concluding synthesis (recap of questions, progressive method, final definitions, seven frameworks, three rules, closing). The damage is localized word/phrase drops, not structural disorder.

---

## Summary

| # | Line | Issue | Severity | Corruption vs. style |
|---|------|-------|----------|----------------------|
| 1 | 7 | Duplicate heading (title repeated as body text) | minor | Corruption (conversion artifact) |
| 2 | 11 | Missing verb ("by  a clear architecture") | major | Corruption |
| 3 | 13 | Missing clause after "clarifies" | major | Corruption |
| 4 | 19 | Missing object ("identify  more precisely") | major | Corruption |
| 5 | 25 | Missing noun in definition ("regulatory  that") | major | Corruption |
| 6 | 29 | Two gaps in emotion definition ("interpretive  through", "organizing  timbre") | major | Corruption (parallel passage on line 21 confirms) |
| 7 | 41 | Fused sentences ("architecture The result") | major | Corruption |
| 8 | 61 | Rule 1 truncated ("omponent with the whole") | critical | Corruption |
| 9 | 63 | Rule 2 gutted ("Second,   with essence"; "but   to establish  identity conditions") | critical | Corruption |
| 10 | 65 | Rule 3 partial ("naming with knowing" without "do not confuse") | major | Corruption |
| 11 | — | 26/37 keys have `0000` placeholder years; 10 missing author, 26 missing year | major | Data quality |
| 12 | — | Multi-source bundles (one key = 3-5 works); CSL author fields mis-parsed | critical | Data quality |
| 13 | — | Near-duplicate numbered keys with overlapping notes | major | Data quality |
| 14 | — | Misleading key names (`group0000work`, title-word suffixes) | minor | Data quality |

**Bottom line:** 10 prose gaps (2 critical, 7 major, 1 minor), all consistent with words dropped during Google Doc conversion — the double/triple spaces mark exactly where text was lost, and none of the gaps read as intentional style. The three-rules passage (lines 61-65), the book's thesis restatement, is the most damaged section and needs the author's source text to repair. Citation keys resolve 1:1 with no orphans, but 70% are placeholder `0000` keys and nearly every entry bundles multiple sources under one key, which defeats traceability and has already produced incorrect CSL author metadata. No prose was reconstructed; all repairs require author approval against the original Google Doc.
