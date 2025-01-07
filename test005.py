"""
验证括号是否有效
"""
def is_valid(s):
    stack = []  # 用栈来存储未闭合的括号
    # 字典，存储每个闭合括号对应的开括号
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_brackets.values():
            # 如果是开括号，压入栈
            stack.append(char)
        elif char in matching_brackets:
            # 如果是闭括号，检查栈顶的开括号是否匹配
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()  # 匹配成功，弹出栈顶元素
            else:
                return False  # 如果栈为空或不匹配，返回 False
    
    return not stack  # 如果栈为空，说明所有括号都匹配，否则返回 False

# 示例使用
s1 = "()[]{}"
s2 = "(]"

print(f"'{s1}' 是否有效: {is_valid(s1)}")
print(f"'{s2}' 是否有效: {is_valid(s2)}")
