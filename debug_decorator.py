from time import ctime


def basic_debug(function):
    def wrapper(*args, **kwargs):
        print "%s : calling function %s with args %s and kwargs %s" % (ctime(), function, args, kwargs)
        result = function(*args, **kwargs)
        print "%s : finished calling function %s" % (ctime(), function)
        print "Result was: %s" % result
    return wrapper

@basic_debug
def say_hello(name="Byte"):
    print "Hello", name
    return True

say_hello(name="Henk")

# Mon Dec  2 16:31:05 2013 : calling function <function say_hello at 0x7f62cb1835f0> \
# with args () and kwargs {'name': 'Henk'}
# Hello Henk
# Mon Dec  2 16:31:05 2013 : finished calling function <function say_hello at 0x7f62cb1835f0>
# Result was: True