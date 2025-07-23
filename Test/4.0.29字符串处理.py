def count_chars(s):
    letters = digits = spaces = others = 0
    for char in s:
        if char.isalpha():  # 字母（包括大小写）
            letters += 1
        elif char.isdigit():  # 数字
            digits += 1
        elif char.isspace():  # 空格（包括制表符、换行符等）
            spaces += 1
        else:  # 其他字符（如标点、符号）
            others += 1
    return letters, digits, spaces, others

# 示例
text = "Hello 123! 你好吗？"
letters, digits, spaces, others = count_chars(text)
print(f"字母: {letters}, 数字: {digits}, 空格: {spaces}, 其他: {others}")