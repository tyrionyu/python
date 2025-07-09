'''
输入圆的半径计算计算周长和面积。
'''
r=int(input('请输入圆的半径：'))

c=2*3.1415926*r

s=3.1415926*r*r

print(f"圆的周长是:{c},圆的面积是:{s}")

print('-'*60)

def func(r):
    sd = 3.1415926*r*r
    cd = 2*3.1415926*r    
    return sd,cd

sd,cd = func(4)

print(f"面积：{sd}, 周长：{cd}")