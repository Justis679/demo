"""
计算一个整数的阶乘。阶乘是所有小于等于该数的正整数的积
"""
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# 示例使用
num = 5
print(f"The factorial of {num} is {factorial(num)}")
