s = "Python3.8"

# 提取数字并转浮点数
num_part = ''.join(filter(str.isdigit, s))          # 提取数字字符"38"
float_num = float(num_part)                         # 转为38.0

# 提取字母并转小写
alpha_part = ''.join(filter(str.isalpha, s)).lower()            # "python"

print(f"字母部分: {alpha_part}, 数字部分: {float_num}")