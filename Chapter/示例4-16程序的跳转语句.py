sum=0
i=1
while i<11:
    sum+=i
    if sum>20:
        print('累加和大于20的当前数是：',i)
        break
    i+=1

print('-'*80)

j=0
while j<3:
    user_name=input('请输入用户名：')
    pwd=input('请输入密码：')
    if user_name=='admin' and pwd=='6666':
        print('系统正在登录，请稍后...')
        break
    else:
        if j<2:
            print('用户名或密码不正确，您还有',2-j,'次机会')
    j+=1
else:
    print('三次均输入错误')
