"""
尾递归
尾递归返回递归函数本身,不会导致栈溢出
"""
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
