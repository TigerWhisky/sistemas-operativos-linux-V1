import os,stat,tempfile
def describe_mode(mode): return stat.filemode(mode)
def main():
    f=tempfile.NamedTemporaryFile(delete=False); path=f.name; f.close()
    try: print(path,describe_mode(os.stat(path).st_mode))
    finally: os.unlink(path)
if __name__=="__main__": main()
