#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,os,platform,re,subprocess,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def meminfo():
 d={}
 for line in Path("/proc/meminfo").read_text().splitlines():
  m=re.match(r"(\w+):\s+(\d+)\s+kB",line)
  if m:d[m.group(1)]=int(m.group(2))*1024
 return d
def vmstat():
 d={}
 for line in Path("/proc/vmstat").read_text().splitlines():
  p=line.split()
  if len(p)==2 and p[1].isdigit():d[p[0]]=int(p[1])
 return d
def main():
 a=argparse.ArgumentParser();a.add_argument("--condition",required=True);a.add_argument("--trace",default=str(ROOT/"results/workload_trace.csv"));a.add_argument("--runs",type=int,default=3);x=a.parse_args()
 out=ROOT/"results/system_experiment.csv";import csv
 base=vmstat()
 for run in range(1,x.runs+1):
  t=time.perf_counter();cp=subprocess.run(["python3",str(ROOT/"src/system_workload.py"),"--trace",x.trace],capture_output=True,text=True,check=True)
  res=json.loads(cp.stdout);now=vmstat();mem=meminfo()
  row={"condition":x.condition,"run":run,"os":platform.platform(),"kernel":platform.release(),"visible_cpus":os.cpu_count(),
       "mem_total_gb":round(mem.get("MemTotal",0)/2**30,3),"mem_available_gb":round(mem.get("MemAvailable",0)/2**30,3),
       "elapsed_s":res["elapsed_s"],"outer_elapsed_s":time.perf_counter()-t,"user_s":res["user_s"],"system_s":res["system_s"],
       "minor_faults":res["minor_faults"],"major_faults":res["major_faults"],"context_switches":res["context_switches"],
       "pgfault_delta":now.get("pgfault",0)-base.get("pgfault",0),"pgmajfault_delta":now.get("pgmajfault",0)-base.get("pgmajfault",0),
       "pswpin_delta":now.get("pswpin",0)-base.get("pswpin",0),"pswpout_delta":now.get("pswpout",0)-base.get("pswpout",0),
       "working_set_mb_per_worker":160,"workers":2,"inner_loops":8,"trace_sha256":hashlib.sha256(Path(x.trace).read_bytes()).hexdigest()}
  exists=out.exists() and out.stat().st_size>0
  with out.open("a",newline="") as f:
   w=csv.DictWriter(f,fieldnames=row.keys())
   if not exists:w.writeheader()
   w.writerow(row)
 base=vmstat()
if __name__=="__main__":main()
