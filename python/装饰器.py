import time

# 写法1:最朴素写法
def run_cal1(func):
    def wrapper():
        timeB = time.time()
        func()
        timeE = time.time()
        print(timeE - timeB)
    return wrapper

@run_cal1
def cal1():
    for i in range(1,1000000):
        print(i)

# 写法2:带有返回值写法
def run_cal2(func):
    def wrapper():
        timeB = time.time()
        result = func() # 带有返回值的函数需要在装饰器函数中将返回值返回出来
        timeE = time.time()
        print(timeE - timeB)
        return result
    return wrapper

@run_cal2
def cal2():
    count = 0
    for i in range(1,1000000):
        count=count+i
    return count


# 写法3:带有参数的函数怎么放进装饰器
def run_cal3(func):
    def wrapper(*args): # 通过*args将原函数的所有参数带入进来
        tB = time.time()
        result = func(*args)
        tE = time.time()
        print(tE-tB)
        return result
    return wrapper

@run_cal3
def cal3(min_value,max_value):
    count=0
    for i in range(min_value,max_value):
        count+=i
    return count



if __name__ == '__main__':
    # 写法1
    #cal1()
    # 写法2
    # print(cal2())
    # 写法3
    print(cal3(1,10))