# Ubuntu/VMware experiment

This is the primary experiment for the term paper.

| Condition | RAM | vCPU |
|---|---:|---:|
| A | 1 GB | 1 |
| B | 2 GB | 1 |
| C | 4 GB | 1 |
| D | 2 GB | 2 |
| E | 2 GB | 4 |

Use the same Ubuntu VM image, workload file, working-set size, and loop count for every condition. Only the VMware RAM/vCPU allocation changes.

## Prepare

```bash
sudo apt update
sudo apt install -y python3 python3-pip
python3 --version
uname -a
lscpu
free -h
bash scripts/prepare_workload.sh
```

Record the SHA-256 workload hash.

## Run

After setting each VMware condition, boot the guest and run:

```bash
bash scripts/run_condition.sh vm_1gb_1vcpu
bash scripts/run_condition.sh vm_2gb_1vcpu
bash scripts/run_condition.sh vm_4gb_1vcpu
bash scripts/run_condition.sh vm_2gb_2vcpu
bash scripts/run_condition.sh vm_2gb_4vcpu
```

Each command records three runs.

## Analyze

```bash
python3 src/analyze_system.py
python3 src/plot_system.py
```

Primary raw data: `results/system_experiment.csv`  
Summary: `results/system_summary.csv`

Do not invent missing measurements.
