# coding=utf-8
# 代码文件：hello.py

import world                # 导入world模块中的所有代码元素
from world import z         # 导入world模块中的变量z
from world import x as x2   # 导入world模块中的变量x，并给它别名x2

x=100
y=20

print(y)
print(world.y)
print(z)
print(x2)