from time import sleep


def sleep_decorator(function):
    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper


@sleep_decorator
def say_hello(name):
    print "Hello", name

print say_hello
# <function wrapper at 0x7fd46ab8f668>
print say_hello("Byte")
# Hello Byte
