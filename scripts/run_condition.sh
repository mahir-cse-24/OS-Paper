#!/usr/bin/env bash
set -euo pipefail
case "$1" in
  vm_1gb_1vcpu|vm_2gb_1vcpu|vm_4gb_1vcpu|vm_2gb_2vcpu|vm_2gb_4vcpu) ;;
  *) echo "Unknown condition"; exit 2 ;;
esac
python3 src/collect_vm_experiment.py --condition "$1" --trace results/workload_trace.csv --runs 3
