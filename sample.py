from poor_profiler import profile
import time

def inner_inner():
    return None

def inner_fn(z):
    print("x", z)
    inner_inner()

@profile
def sample(x):
    print("a")
    time.sleep(1)
    inner_fn(4)
    print("b")
    time.sleep(2)
    print("c")
    print("d")


sample(1)
