class counter(object):
    def __init__(self, function):
        self.function = function
        self.counter = 0

    def call_count(self):
        return self.counter

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.function(*args, **kwargs)


@counter
def hello(name):
    print "Hello, %s" % name

for i in range(0, 3):
    hello("Byte")

print type(hello)
print hello.call_count()

# Hello, Byte
# Hello, Byte
# Hello, Byte
# <class '__main__.counter'>
# 3