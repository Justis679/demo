# 读取文件内容
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# 写入文件
with open('example_output.txt', 'w') as file:
    file.write("Hello, this is a test!")
