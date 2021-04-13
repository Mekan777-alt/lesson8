def type_logger(function):

    def decor_funct(*args):
        for a in args:
            print(function.__name__,(a, type(a)))

    return decor_funct


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(3, 2, 1)