from multiprocessing import Process, shared_memory

def child(name):
    shm = shared_memory.SharedMemory(name=name)
    try:
        shm.buf[:5] = b"CHILD"
    finally:
        shm.close()

if __name__ == "__main__":
    shm = shared_memory.SharedMemory(create=True, size=32)
    try:
        shm.buf[:5] = b"PARENT"
        p = Process(target=child, args=(shm.name,))
        p.start()
        p.join()
        print(bytes(shm.buf[:5]).decode())
    finally:
        shm.close()
        shm.unlink()
