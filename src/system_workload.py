#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,resource,time
from multiprocessing import Process,Queue
from pathlib import Path
PAGE=4096
def lcg(seed:int)->int:return (1664525*seed+1013904223)&0xffffffff
def build_trace(path:Path,steps:int,pages:int,seed:int=3072026)->None:
    path.parent.mkdir(parents=True,exist_ok=True);x=seed&0xffffffff
    with path.open("w",newline="") as f:
        w=csv.writer(f);w.writerow(["step","worker","page_index"])
        for step in range(steps):
            for worker in (0,1):
                x=lcg(x);w.writerow([step,worker,x%pages])
def load_trace(path:Path,worker:int):
    with path.open() as f:return [int(r["page_index"]) for r in csv.DictReader(f) if int(r["worker"])==worker]
def worker(wid,trace_path,working_set_mb,inner_loops,q):
    trace=load_trace(Path(trace_path),wid);pages=max(1,working_set_mb*1024*1024//PAGE);buf=bytearray(pages*PAGE)
    t=time.perf_counter();checksum=0
    for _ in range(inner_loops):
        for idx in trace:
            p=(idx%pages)*PAGE;v=(buf[p]+wid+1)&255;buf[p]=v;checksum=(checksum+v)&0xffffffff
    ru=resource.getrusage(resource.RUSAGE_SELF)
    q.put({"worker":wid,"elapsed_s":time.perf_counter()-t,"user_s":ru.ru_utime,"system_s":ru.ru_stime,
           "minor_faults":ru.ru_minflt,"major_faults":ru.ru_majflt,
           "voluntary_ctx":ru.ru_nvcsw,"involuntary_ctx":ru.ru_nivcsw,"checksum":checksum})
def main():
    a=argparse.ArgumentParser();a.add_argument("--trace",type=Path,required=True);a.add_argument("--working-set-mb",type=int,default=160);a.add_argument("--inner-loops",type=int,default=8);x=a.parse_args()
    q=Queue();ps=[Process(target=worker,args=(w,str(x.trace),x.working_set_mb,x.inner_loops,q)) for w in (0,1)]
    t=time.perf_counter()
    for p in ps:p.start()
    rows=[q.get() for _ in ps]
    for p in ps:p.join()
    print(json.dumps({"elapsed_s":time.perf_counter()-t,"workers":2,"working_set_mb_per_worker":x.working_set_mb,
      "inner_loops":x.inner_loops,"user_s":sum(r["user_s"] for r in rows),"system_s":sum(r["system_s"] for r in rows),
      "minor_faults":sum(r["minor_faults"] for r in rows),"major_faults":sum(r["major_faults"] for r in rows),
      "context_switches":sum(r["voluntary_ctx"]+r["involuntary_ctx"] for r in rows)}))
if __name__=="__main__":main()
