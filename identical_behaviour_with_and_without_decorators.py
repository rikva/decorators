## Decorator doing nothing
def decorator(*args, **kwargs):
    def wrapper(*args, **kwargs):
        def innerwrapper(*args, **kwargs):
            pass
        return innerwrapper
        pass
    return wrapper
    pass


################################
## Decorator without argument ##
################################

#####################
## With decorator: ##
#####################


@decorator
def my_function(tomato=False):
    if tomato:
        print "Yummy"

print my_function
# <function wrapper at 0x7f684720e668>

my_function(tomato=True)
# Actual full call:  decorator(my_function)(tomato=True)


########################
## without decorator: ##
########################


def my_function(tomato=True):
    if tomato:
        print "Yummy"
my_function = decorator(my_function)

print my_function
# <function wrapper at 0x7f684720e668>

my_function(tomato=True)
# Actual full call:  decorator(my_function)(tomato=True)

#############################
## Decorator with argument ##
#############################


#####################
## With decorator: ##
#####################


@decorator(logging=True)
def my_function(tomato=False):
    if tomato:
        print "Yummy"

print my_function
# <function innerwrapper at 0x7fcfa995a5f0>

my_function(tomato=True)
# Actual full call:  decorator(logging=True)(my_function)(tomato=True)


########################
## without decorator: ##
########################

def my_function(tomato=True):
    if tomato:
        print "Yummy"
my_function = decorator(logging=True)(my_function)

print my_function
# <function innerwrapper at 0x7fcfa995a5f0>

my_function(tomato=True)
# Actual full call:  decorator(logging=True)(my_function)(tomato=True)

