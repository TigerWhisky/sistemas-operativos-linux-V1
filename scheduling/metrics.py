def calculate_metrics(processes, completion, first_start):
    result = {}
    for p in processes:
        turnaround = completion[p.name] - p.arrival
        result[p.name] = {
            "completion": completion[p.name],
            "turnaround": turnaround,
            "waiting": turnaround - p.burst,
            "response": first_start[p.name] - p.arrival,
        }
    return result
