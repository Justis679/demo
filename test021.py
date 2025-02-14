def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2024-6-1')

"""
把@log放到now()函数的定义处相当于 now = log(now) ，执行now() 等于执行log(now)()
"""
