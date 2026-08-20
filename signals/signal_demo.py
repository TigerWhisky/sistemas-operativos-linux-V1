import signal, time

running = True

def stop(signum, frame):
    global running
    print("received:", signum)
    running = False

signal.signal(signal.SIGINT, stop)
signal.signal(signal.SIGTERM, stop)

print("running; use Ctrl+C or SIGTERM")
while running:
    time.sleep(.5)
print("clean shutdown")
