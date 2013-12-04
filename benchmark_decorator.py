import time
from datetime import datetime


def benchmark(function):
    def wrapper(*args, **kwargs):
        begin = datetime.now()
        result = function(*args, **kwargs)
        end = datetime.now()
        delta = end - begin
        print "Calling %s took %d seconds." % (function.__name__, delta.seconds)
        return result
    return wrapper


@benchmark
def wait(secs=2):
    time.sleep(secs)


wait()
# Calling wait took 2 seconds.

