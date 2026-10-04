# Submission checklist

## Before submission

- [ ] Run all five Ubuntu/VMware conditions.
- [ ] Reuse the identical workload trace for every condition.
- [ ] Confirm the trace hash is unchanged.
- [ ] Collect three runs per condition.
- [ ] Run the analysis and plotting scripts.
- [ ] Replace the pending primary result values in the LaTeX report with measured values.
- [ ] Compile the final 3–4 page PDF.
- [ ] Check tables, figures, references, student information, and page count.
- [ ] Run repository tests.

## Submit

1. GitHub repository: https://github.com/mahir-cse-24/OS-Paper
2. Final compiled PDF.
3. Printed report if required by the course.
4. 3–5 minute walkthrough/demo.

## Walkthrough

1. Research question and five VM configurations.
2. One fixed workload used for every condition.
3. Ubuntu measurements: timing, CPU, page faults, context switches, and swap.
4. Interpretation using memory-management and virtualization concepts.
5. Briefly show the retained predictive placement extension.

## Result integrity

Only measurements actually collected inside the Ubuntu VMware guest should appear in the primary experimental results.
