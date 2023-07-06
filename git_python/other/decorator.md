# Decorator

### 1. 函数作为参数

```PYTHON
def double(x):
    return x * 2

def triple(x):
    return x * 3


def calc_numbet(func,x):
    return func(x)

print(calc_numbet(double,3))
print(calc_numbet(triple,3))
```

这里定义了两个函数double与triple, 以及函数calc_numbet,使用calc_numbet对double与triple进行调用,这是一个函数作为参数的直观例子



## 2. 函数作为返回值

```python
def get_multiple_func(n):
    def multiple(x):
        return x * n

    return multiple

print(get_multiple_func(3)(2))
print(get_multiple_func(3)(3))
```

get_multiple_func的返回值是一个函数multiple,而multiple的一部分参数通过get_multiple_func获取



## 3.不带参数的Decorator

```python
def timeit(f):
    def wrapper(x):
        print(x)
        start_time = time.time()
        print(f)
        ret = f(x)
        end_time = time.time()
        print(end_time - start_time)
        return ret

    return wrapper

@timeit
def myfunc(x):
    time.sleep(x)

myfunc(10)
```



## 4. 带参数的Decorator

```
import time
def timeititer(iteration):
    def inner(f):
        def wrapper(*args,**kwargs):
            start_time = time.time()
            for _ in range(iteration):
                ret = f(*args,**kwargs)
            end_time = time.time()
            print(end_time-start_time)
            return ret
        return wrapper
    return inner

@timeititer(1000)
def double(x):
    return x * 2

double(2)
```









