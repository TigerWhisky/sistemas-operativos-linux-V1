# LAB-15 — System calls

```bash
gcc -Wall -Wextra -O2 src/syscalls/file_syscalls.c -o /tmp/file_syscalls
/tmp/file_syscalls
gcc -Wall -Wextra -O2 src/syscalls/process_syscalls.c -o /tmp/process_syscalls
/tmp/process_syscalls
```

Quando disponível:
```bash
strace /tmp/file_syscalls
```
