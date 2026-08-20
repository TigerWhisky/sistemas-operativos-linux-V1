from scheduling.models import Process
from scheduling.fcfs import schedule as fcfs
from scheduling.sjf import schedule as sjf
from scheduling.priority import schedule as priority
from scheduling.round_robin import schedule as rr

def show(name, result):
    order, metrics = result
    print("\n"+name)
    print("Gantt:", " | ".join(f"{p}:{a}-{b}" for p,a,b in order))
    for p,m in metrics.items(): print(p,m)

if __name__ == "__main__":
    ps=[Process("P1",0,8,2),Process("P2",1,4,1),
        Process("P3",2,2,3),Process("P4",3,5,2)]
    show("FCFS",fcfs(ps))
    show("SJF",sjf(ps))
    show("Priority",priority(ps))
    show("Round Robin q=2",rr(ps,2))
