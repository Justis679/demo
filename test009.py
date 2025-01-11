"""
判断一个数是否为质数可以使用以下方法，时间复杂度较低
"""
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # 输出: True
print(is_prime(10))  # 输出: False
