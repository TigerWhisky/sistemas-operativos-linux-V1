from threading import Semaphore, Thread
import time

sem = Semaphore(2)

def worker(i):
    print(i, "waiting")
    with sem:
        print(i, "using resource")
        time.sleep(.2)
    print(i, "released")

if __name__ == "__main__":
    ts = [Thread(target=worker, args=(i,)) for i in range(6)]
    for t in ts: t.start()
    for t in ts: t.join()
