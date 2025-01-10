"""
用 get() 获取字典的值
当访问字典的键时，如果键不存在，使用 get() 方法可以避免抛出 KeyError，并返回一个默认值（默认是 None）。
"""
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))  # 输出: Alice
print(person.get('gender', 'Unknown'))  # 输出: Unknown
