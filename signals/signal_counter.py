import os, signal, time
count = 0
running = True

def usr1(signum, frame):
    global count
    count += 1
    print("SIGUSR1:", count)

def term(signum, frame):
    global running
    running = False

signal.signal(signal.SIGUSR1, usr1)
signal.signal(signal.SIGTERM, term)
print("PID:", os.getpid())
while running:
    time.sleep(.5)
print("final count:", count)
