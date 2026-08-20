import os

def main():
    print(f"parent PID={os.getpid()}")
    pid = os.fork()
    if pid == 0:
        print(f"child PID={os.getpid()} PPID={os.getppid()}")
        os.execlp("python3", "python3", "-c",
                  "import os; print('exec PID=', os.getpid())")
    waited, status = os.waitpid(pid, 0)
    print(f"waitpid PID={waited} status={status}")

if __name__ == "__main__":
    main()
