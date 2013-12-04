
class ClassDecorator(object):
    def __init__(self, function):
        pass


def function_decorator(function):
    def wrapper(*args, **kwargs):
        pass
    return wrapper


@ClassDecorator
def my_function():
    print "Welcome commander"


print my_function
# <__main__.ClassDecorator object at 0x7fe0f1796c50>

@function_decorator
def my_function():
    print "Welcome commander"


print my_function
# <function wrapper at 0x7fe0f17986e0>

