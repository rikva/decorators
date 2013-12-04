from time import sleep


def tunable_sleep_decorator(seconds):
    def decorator(function):
        def wrapper(*args, **kwargs):
            sleep(seconds)
            return function(*args, **kwargs)
        return wrapper
    return decorator


@tunable_sleep_decorator(seconds=1)
def say_hello(name):
    print "Hello", name


print say_hello
say_hello("Byte")