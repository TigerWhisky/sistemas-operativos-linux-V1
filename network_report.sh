#!/usr/bin/env bash
set -euo pipefail
ip -br addr
ip route
ss -tuln
