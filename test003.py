"""
计算一个列表中的所有数字之和，并返回大于给定阈值的数字个数
"""
def process_list(numbers, threshold):
    # 计算列表中所有数字的和
    total_sum = sum(numbers)
    
    # 计算大于阈值的数字个数
    count_above_threshold = len([num for num in numbers if num > threshold])
    
    return total_sum, count_above_threshold

# 示例使用
numbers = [10, 20, 30, 40, 50]
threshold = 25

total_sum, count_above_threshold = process_list(numbers, threshold)
print(f"数字和: {total_sum}")
print(f"大于阈值的数字个数: {count_above_threshold}")
