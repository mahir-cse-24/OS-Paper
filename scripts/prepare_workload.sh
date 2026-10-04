#!/usr/bin/env bash
set -euo pipefail
mkdir -p results figures
python3 src/system_workload.py --trace results/workload_trace.csv >/dev/null 2>&1 || true
# Generate a 2000-step deterministic trace.
python3 - <<'PY'
from pathlib import Path
import sys
sys.path.insert(0,"src")
from system_workload import build_trace
build_trace(Path("results/workload_trace.csv"),steps=2000,pages=8192,seed=3072026)
PY
sha256sum results/workload_trace.csv
