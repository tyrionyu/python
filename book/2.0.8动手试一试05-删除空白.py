""" full_name=" Yu Zhengjia     "
rstrip_name=full_name.rstrip()
print(rstrip_name,end='\t')
lstrip_name=full_name.lstrip()
print(lstrip_name,end='\n')

result=full_name.strip()
print(result) """

name = "\tEric Matthes\n"

print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())    #去除左边字符

print("\nUsing rstrip():")
print(name.rstrip())    #去除右边字符

print("\nUsing strip():")
print(name.strip())     #去除左右两边字符
