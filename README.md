# Sistemas Operativos Linux — v1.0

Projeto prático de estudo sobre Sistemas Operativos em Linux.

## Conteúdos
- Processos: fork, exec, wait
- Sinais Unix/Linux
- IPC: memória partilhada
- Threads e sincronização
- Semáforos
- Deadlocks
- Escalonamento CPU: FCFS, SJF, Priority e Round Robin
- Métricas de escalonamento
- Memória virtual e page replacement
- System calls em C
- Filesystems e permissões
- Monitorização Linux
- Testes automatizados

## Instalação
Linux/Unix, Python 3.11+, GCC e Bash.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -v
```

## Simulador CPU
```bash
python3 src/scheduling/simulator.py
```

Algoritmos: FCFS, SJF, Priority e Round Robin.

## System calls
```bash
gcc -Wall -Wextra -O2 src/syscalls/file_syscalls.c -o /tmp/file_syscalls
/tmp/file_syscalls
```

Quando disponível:
```bash
strace /tmp/file_syscalls
```

