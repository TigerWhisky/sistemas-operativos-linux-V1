import threading
ITERATIONS=100_000
THREADS=4

def run_once():
    counter=0; lock=threading.Lock()
    def inc():
        nonlocal counter
        for _ in range(ITERATIONS):
            with lock: counter+=1
    ts=[threading.Thread(target=inc) for _ in range(THREADS)]
    for t in ts:t.start()
    for t in ts:t.join()
    return counter
