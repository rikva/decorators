from time import sleep

# Lacks nesting


def broken_sleep_decorator(function):
    print "Calling"
    sleep(1)
    return function


@broken_sleep_decorator
def say_hello(name):
    print "Hello", name


print say_hello

say_hello("Byte")