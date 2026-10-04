#!/usr/bin/env python3
import pandas as pd,matplotlib.pyplot as plt
from pathlib import Path
d=pd.read_csv("results/system_summary.csv");Path("figures").mkdir(exist_ok=True)
for m,y,f in [("mean_elapsed_s","Mean elapsed time (s)","system_elapsed.png"),("mean_major_faults","Mean major page faults","system_major_faults.png"),("mean_pswpout_delta","Mean pages swapped out","system_swap_out.png")]:
 plt.figure(figsize=(7,4));plt.bar(d.condition,d[m]);plt.xlabel("VM condition");plt.ylabel(y);plt.xticks(rotation=25,ha="right");plt.tight_layout();plt.savefig("figures/"+f,dpi=180);plt.close()
