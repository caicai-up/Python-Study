"""
定义获取程序的执行时间装饰器
"""
import time

def getTime(fn):
    def inner(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print(f"程序执行了：{end - start}s")

    return inner

@getTime
def compute():
    time.sleep(3)


compute()

"""
定义一个装饰器可以指定参数打印日志
"""
def log(flag):
    def decorator(fn):
        def inner(*args, **kwargs):
            if flag == "+":
                print("正在执行加法计算")
            elif flag == "-":
                print("正在执行减法计算")
            return fn(*args, **kwargs)

        return inner

    return decorator

@log("+")
def add(a, b):
    return a + b

@log("-")
def minus(a, b):
    return a - b


print(add(1, 2))
print(minus(2, 1))
