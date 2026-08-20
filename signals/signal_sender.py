import os, signal, sys
if len(sys.argv) != 2:
    raise SystemExit("usage: python3 signal_sender.py PID")
pid = int(sys.argv[1])
os.kill(pid, signal.SIGUSR1)
print("SIGUSR1 sent to", pid)
