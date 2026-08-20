from memory.page_replacement import fifo_references,lru_references
def test_fifo(): assert fifo_references([1,2,3,1,4],3)[0]==4
def test_lru(): assert lru_references([1,2,3,1,4],3)[0]==4
