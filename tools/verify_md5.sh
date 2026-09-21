#!/usr/bin/env bash
# ตรวจ md5 ของทุกไฟล์เทียบ MANIFEST.md5 — exit 1 ถ้าไม่ตรง/ไฟล์หาย
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO" || exit 2
[[ -f MANIFEST.md5 ]] || { echo "MANIFEST.md5 not found in $REPO"; exit 2; }

checked=0; failed=0
while read -r want path; do
  [[ -z "${want:-}" ]] && continue
  checked=$((checked+1))
  if [[ ! -f "$path" ]]; then echo "MISSING   $path"; failed=$((failed+1)); continue; fi
  got="$(md5 -q "$path")"
  if [[ "$got" != "$want" ]]; then
    echo "MISMATCH  $path"; echo "  want=$want"; echo "  got =$got"; failed=$((failed+1))
  fi
done < MANIFEST.md5

echo "checked=$checked failed=$failed"
if [[ $failed -eq 0 ]]; then echo "OK"; exit 0; else exit 1; fi
