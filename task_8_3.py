def type_logger(func):
    def wrapped(*args):
        res = func(*args)
        if len(args) == 1:
            print(args[0], ":", type(args[0]))
        else:
            for el in args:
                print(el, ":", type(el))
        return res

    return wrapped


@type_logger
def calc_cube(x, *args):
    return x ** 3


func_name = calc_cube(7)
print(func_name)
