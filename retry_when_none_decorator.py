from time import sleep


def retry_if_result_is_none(max_retries=3, secs_delay_between_tries=1):
    def decorator(function):
        def wrapper(*f_args, **f_kwargs):
            counter = 0
            while counter <= max_retries:
                counter += 1
                print "Attempt %d of %d" % (counter, max_retries+1)
                result = function(*f_args, **f_kwargs)
                if result is not None:
                    return result
                sleep(secs_delay_between_tries)
            else:
                raise RuntimeError("Failed after %d attempts!" % counter)
        return wrapper
    return decorator


@retry_if_result_is_none(max_retries=2, secs_delay_between_tries=0)
def return_none():
    print "Returning None"
    return


return_none()
# Attempt 1 of 3
# Returning None
# Attempt 2 of 3
# Returning None
# Attempt 3 of 3
# Returning None
# Traceback (most recent call last):
# RuntimeError: Failed after 3 attempts!