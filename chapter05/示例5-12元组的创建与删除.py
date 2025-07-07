t=('Hello',[10,20,30],'Python','World')
print(t)

#使用内置函数tuple()创建元组
t=tuple('HelloWorld')
print(t)

t2=tuple([10,20,30,40])
print(t2)

print('10在元组中是否存在：',(10 in t2))
print('10在元组是否存在：',(10 not in t2))
print('最大值：',(10 not in t2))
print('最小组：',(10 not in t2))
print('len：',(10 not in t2))
print('t2.index：',t2.index(10))
print('t2.count：',t2.count(10))

#如果元组只有一个元素
t3=(10)
print(t3,type(t3))

#如果元素中只有一个元素，逗号不能省
y=(10,)
print(y,type(y))

#元组的删除
del y
print(y)