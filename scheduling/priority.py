from .metrics import calculate_metrics

def schedule(processes):
    remaining=list(processes); now=0; completion={}; first={}; order=[]
    while remaining:
        ready=[p for p in remaining if p.arrival<=now]
        if not ready:
            now=min(p.arrival for p in remaining); continue
        p=min(ready,key=lambda x:(x.priority,x.arrival,x.name))
        remaining.remove(p); first[p.name]=now
        order.append((p.name,now,now+p.burst)); now+=p.burst
        completion[p.name]=now
    return order, calculate_metrics(processes,completion,first)
