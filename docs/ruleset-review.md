# Branch Protection Ruleset Review

**Ruleset:** Protect Canonical Manuscript (ID: 24886363)
**Target:** `refs/heads/main`
**Status:** Active
**Reviewed:** 2026-10-11

## Current Configuration

| Rule | Setting |
|------|---------|
| Deletion protection | Enabled |
| Non-fast-forward protection | Enabled |
| Required approving reviews | 1 |
| Dismiss stale reviews on push | Yes |
| Require code owner review | **No** (should be Yes) |
| Required review thread resolution | Yes |
| Required status checks | **Empty** (should list CI checks) |
| Allowed merge methods | merge, squash, rebase |

## Bypass Exception (Documented)

**Actor:** cezjah (User ID: 13968367)
**Mode:** `always`

This bypass allows the repository owner to push directly to main without
going through pull request review. This is intentional per author request:
"admins must not be locked out of main."

The bypass does NOT disable deletion or force-push protection for other actors.

## Changes Applied (Author Approved 2026-10-11)

1. **Required status checks:** Added `validate` job from `validate-manuscript.yml`
   - Manuscript validation must pass before merge to main

2. **Code owner review:** Enabled `require_code_owner_review: true`
   - CODEOWNERS covers `/.github/workflows/`, `/publishing/`, `/scripts/`
   - Infrastructure changes now require owner review

3. **Strict status checks:** Not enabled (left as `false` per conservative default)

## Bypass Exception

Unchanged. cezjah retains `bypass_mode: always` per author request.
