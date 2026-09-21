#!/usr/bin/env bash
# ดึงต้นทางล่าสุดจาก GitHub (sealfx) แล้วสร้าง EFI-OSX86 ใหม่ — idempotent
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(dirname "$HERE")"
ROOT="$(dirname "$REPO")"
UP="$ROOT/_recon/upstream"
mkdir -p "$UP"

while read -r name branch; do
  [ -z "${name:-}" ] && continue
  if [ -d "$UP/$name/.git" ]; then
    echo "== fetch $name ($branch)"
    git -C "$UP/$name" fetch --depth 1 origin "$branch"
    git -C "$UP/$name" reset --hard FETCH_HEAD
  else
    echo "== clone $name ($branch)"
    GIT_TERMINAL_PROMPT=0 git clone --depth 1 --branch "$branch" "https://github.com/sealfx/$name.git" "$UP/$name"
  fi
done < <(python3 "$HERE/build.py" --list-repos)

echo "== build"
python3 "$HERE/build.py"
echo "== verify"
bash "$HERE/verify_md5.sh"
