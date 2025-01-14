"""
生成一个指定长度的随机密码，包含字母、数字和特殊字符
"""
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# 示例使用
print("Generated password:", generate_password(12))
