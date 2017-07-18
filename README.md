See sample.py for an example.   Running a function decorated with "@profile"
should print out warnings whenever a line takes > 0.5 seconds to execute.

See sample.py for an example.  Executing "python sample.py" should print:

```
The next line will sleep for 1 second
sample.py(14): 1.002 secs elapsed
The next line is fast
The next line will sleep for 2 seconds
sample.py(17): 2.005 secs elapsed
...and some quick print statements...
...which should be ignored...
...by the profiler because they're quick.
```
