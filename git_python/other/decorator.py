def double(x):
    return x * 2

def triple(x):
    return x * 3


def calc_numbet(func,x):
    return func(x)


print(calc_numbet(double,3))
print(calc_numbet(triple,3))

# 函数的返回值也可以是一个函数
def get_multiple_func(n):
    def multiple(x):
        return x * n

    return multiple

print(get_multiple_func(3)(2))
print(get_multiple_func(3)(3))





@timeit
def other_func(x):
    return x * 2

print(other_func(2))






