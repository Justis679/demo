
def count_characters(s):
    # 创建一个空字典用来存储字符的出现次数
    char_count = {}
    
    # 遍历字符串中的每个字符
    for char in s:
        if char in char_count:
            # 如果字符已经在字典中，增加其计数
            char_count[char] += 1
        else:
            # 如果字符不在字典中，添加并将计数设为1
            char_count[char] = 1
            
    return char_count

# 示例使用
s = "apple"
result = count_characters(s)
print(result)
