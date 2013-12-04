def pass_on_argument(function):
    def function_being_returned(name="Byte"):
        return function(name=name)
    return function_being_returned


class PassOnArgument(object):
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        return self.function(name="Byte")