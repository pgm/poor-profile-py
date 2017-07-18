import sys
from functools import wraps
from time import time

co_profiled = set()

def profile(fn, min_time=0.5):
    co_profiled.add(id(fn.func_code))
    prev = [time(), None, None]
    
    def _next_line(frame, event, arg):
        if event == "line":
            t = time()
            prev_time, prev_filename, prev_lineno = prev
            elapsed = t - prev_time
            prev[0] = t
            prev[1] = frame.f_code.co_filename
            prev[2] = frame.f_lineno
            
            if elapsed > min_time:           
                print("{}({}): {:.3f} secs elapsed".format( prev_filename, prev_lineno, elapsed))

        return None
    
    def next_line(frame, event, arg):
        if event == "call":
            if id(frame.f_code) in co_profiled:
                return _next_line
        return None

    @wraps(fn)
    def wrapper(*args, **kwargs):
        prev_trace = sys.gettrace()
        try:
            sys.settrace(next_line)
            return fn(*args, **kwargs)
        finally:
            sys.settrace(prev_trace)

    return wrapper

    