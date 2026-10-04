from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from system_workload import build_trace, load_trace
def test_trace_is_deterministic(tmp_path):
    a,b=tmp_path/"a.csv",tmp_path/"b.csv"
    build_trace(a,20,128,3072026); build_trace(b,20,128,3072026)
    assert a.read_bytes()==b.read_bytes()
def test_two_workers_have_same_number_of_references(tmp_path):
    p=tmp_path/"trace.csv"; build_trace(p,40,64,1)
    assert len(load_trace(p,0))==40 and len(load_trace(p,1))==40
