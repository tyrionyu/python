s=input().split()

if s[2] not in ['+','-','*','/']:
    print('PPPP')
elif (s[2]=='/') and (int(s[1])==0):
    print('不能为零')
else:
    print(int(eval(s[0]+s[2]+s[1])))