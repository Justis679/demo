
def find_duplicates(nums):
    # 使用集合来跟踪已经看到的元素
    seen = set()
    duplicates = set()
    
    # 遍历列表，找出重复元素
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    # 返回重复元素的列表
    return list(duplicates)

# 示例使用
nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]
result = find_duplicates(nums)
print(f"重复元素: {result}")
