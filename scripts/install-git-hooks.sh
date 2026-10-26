#!/usr/bin/env bash
# Installs the pre-push hook that runs scripts/commit-guard.sh. Re-run once per fresh clone.
set -e
root=$(git rev-parse --show-toplevel)
hook="$root/.git/hooks/pre-push"
cat > "$hook" <<'HOOK'
#!/usr/bin/env bash
exec bash "$(git rev-parse --show-toplevel)/scripts/commit-guard.sh"
HOOK
chmod +x "$hook"
git config user.name "ba-00001"
git config user.email "124537281+ba-00001@users.noreply.github.com"
echo "pre-push hook installed at $hook"
