def contest(func):
    def wraper(*args, **kwargs):
        with func(*args, **kwargs) as f:
            return f(*args, **kwargs)

    return wraper


@contest
def some(name):
    return a + 1


print(some(5))
