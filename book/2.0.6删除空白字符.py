language=" Python "

'''要将字符串中的空白永久删除，需把值赋值给变量才行。'''
'''删除右侧字符串'''
result_rstip=language.rstrip()
print(result_rstip)

'''删除左侧字符'''
result_lstip=language.lstrip()
print(result_lstip)

'''同时删除两边的空白'''
result_strip=language.strip()
print(result_strip)

'''常用于删除用户空白字符串，如用户名'''