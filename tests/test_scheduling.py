from scheduling.models import Process
from scheduling.fcfs import schedule as fcfs
from scheduling.sjf import schedule as sjf
from scheduling.priority import schedule as priority
from scheduling.round_robin import schedule as rr

P=[Process("P1",0,8,2),Process("P2",1,4,1),Process("P3",2,2,3),Process("P4",3,5,2)]

def test_fcfs(): assert fcfs(P)[1]["P4"]["completion"]==19
def test_sjf(): assert sjf(P)[0][0][0]=="P1"
def test_priority(): assert priority(P)[0][1][0]=="P2"
def test_rr(): assert rr(P,2)[1]["P1"]["completion"]>0
def test_invalid_quantum():
    try: rr(P,0); assert False
    except ValueError: pass
