from collections import deque
from .metrics import calculate_metrics

def schedule(processes, quantum=2):
    if quantum <= 0: raise ValueError("quantum must be positive")
    pending=sorted(processes,key=lambda x:(x.arrival,x.name))
    q=deque(); now=0; i=0
    remaining={p.name:p.burst for p in processes}
    completion={}; first={}; order=[]
    while i<len(pending) or q:
        if not q: now=max(now,pending[i].arrival)
        while i<len(pending) and pending[i].arrival<=now:
            q.append(pending[i]); i+=1
        p=q.popleft()
        first.setdefault(p.name,now)
        run=min(quantum,remaining[p.name])
        order.append((p.name,now,now+run))
        now+=run; remaining[p.name]-=run
        while i<len(pending) and pending[i].arrival<=now:
            q.append(pending[i]); i+=1
        if remaining[p.name]: q.append(p)
        else: completion[p.name]=now
    return order, calculate_metrics(processes,completion,first)
