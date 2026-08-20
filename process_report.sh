#!/usr/bin/env bash
set -euo pipefail
ps -eo pid,ppid,user,stat,%cpu,%mem,comm --sort=-%cpu | head -n 20
