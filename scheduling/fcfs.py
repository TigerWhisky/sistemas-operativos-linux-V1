from .metrics import calculate_metrics

def schedule(processes):
    now = 0; completion = {}; first = {}; order = []
    for p in sorted(processes, key=lambda x:(x.arrival,x.name)):
        now = max(now, p.arrival)
        first[p.name] = now
        order.append((p.name, now, now+p.burst))
        now += p.burst
        completion[p.name] = now
    return order, calculate_metrics(processes, completion, first)
