import threading,time
a=threading.Lock(); b=threading.Lock()
def one():
    with a:
        time.sleep(.2)
        with b: pass
def two():
    with b:
        time.sleep(.2)
        with a: pass
if __name__=="__main__":
    x=threading.Thread(target=one); y=threading.Thread(target=two)
    x.start(); y.start(); x.join(); y.join()
