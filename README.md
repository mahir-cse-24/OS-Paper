# CSE-307 Term Paper

## VM Resource Effects on an Ubuntu Workload

**Student:** Lt Chowdhury Mahir Muhibbullah  
**Student ID:** 202214172  
**Section:** CSE-24  
**Course:** CSE-307 Operating Systems, Spring 2026

The main study measures the same fixed workload inside an Ubuntu VMware guest under five resource configurations. The repository also retains the earlier predictive VM-placement study as a separate extension.

| Condition | RAM | vCPU |
|---|---:|---:|
| A | 1 GB | 1 |
| B | 2 GB | 1 |
| C | 4 GB | 1 |
| D | 2 GB | 2 |
| E | 2 GB | 4 |

The workload trace is generated once and reused for every condition. Measurements include elapsed time, CPU time, page faults, context switches, swap activity, visible CPU count, and guest memory information.

## Run

Inside the Ubuntu guest:

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

Do not replace VMware measurements with guessed or simulated values.

## Extension

The retained Track 4 extension includes First-Fit, Best-Fit, regression-based near-future VM load prediction, a demand shift, utilization balance, overload/SLA events, migrations, predictor ablation, threshold sensitivity, and explanation-confidence analysis.

## Submission

Submit this GitHub repository and the compiled 3–4 page PDF through the course submission channel. See `SUBMISSION.md` and `VMWARE_EXPERIMENT.md`.
