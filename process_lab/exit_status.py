import os

pid = os.fork()
if pid == 0:
    os._exit(7)
waited, status = os.waitpid(pid, 0)
print("PID:", waited)
print("exit code:", os.WEXITSTATUS(status))
