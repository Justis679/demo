"""
正则表达式提取电子邮件地址
"""
import re

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

# 示例：提取电子邮件地址
text = "Contact us at support@example.com or sales@company.org."
emails = extract_emails(text)
print("Extracted emails:", emails)
