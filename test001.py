def is_palindrome(x):
    # 特殊情况：负数或最后一位为0（但不为0本身）直接返回False
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # 回文数的两种情况：长度为偶数或奇数
    return x == reversed_half or x == reversed_half // 10

# 测试
print(is_palindrome(121))  # True
print(is_palindrome(-121))  # False
print(is_palindrome(10))  # False
