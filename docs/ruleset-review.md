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

## Recommended Changes (Require Author Approval)

The following changes are recommended but NOT applied, pending author approval
per QA feedback item #8:

1. **Add required status checks:**
   - `validate` job from `validate-manuscript.yml` workflow
   - This ensures manuscript validation passes before merge

2. **Enable code owner review:**
   - Set `require_code_owner_review: true`
   - CODEOWNERS already covers `/.github/workflows/`, `/publishing/`, `/scripts/`
   - This ensures infrastructure changes get owner review

3. **Consider strict status checks:**
   - Set `strict_required_status_checks_policy: true`
   - Requires branches to be up-to-date before merging

## Approval Request

These administrative changes require explicit author approval before implementation.
See QA feedback item #8.
