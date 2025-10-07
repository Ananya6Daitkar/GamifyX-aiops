# Runbook / Rollback

## Quick rollback
- For this demo, "rollback" is a manual step:
  1. Revert the deploy commit: `git revert <deploy-commit>`
  2. Push to main, Actions will deploy reverted version.
- In real infra: use the registry to `docker pull <previous-tag>` and redeploy.

## Smoke test checklist
- /api/status returns 200
- leaderboard endpoint functions
- No obvious errors in logs
