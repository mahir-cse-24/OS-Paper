# Run guide

```bash
bash scripts/prepare_workload.sh
bash scripts/run_condition.sh vm_1gb_1vcpu
bash scripts/run_condition.sh vm_2gb_1vcpu
bash scripts/run_condition.sh vm_4gb_1vcpu
bash scripts/run_condition.sh vm_2gb_2vcpu
bash scripts/run_condition.sh vm_2gb_4vcpu
python3 src/analyze_system.py
python3 src/plot_system.py
```

The same trace is used across all five conditions.
