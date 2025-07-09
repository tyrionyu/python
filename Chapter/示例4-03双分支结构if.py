num=eval(input('请输入您的六位中奖号码：'))
if num==654321:
    print('恭喜您中奖了！')
else:
    print('您本期未中大奖！')

print('以上代码可以使用条件表达式进行简化')
result='恭喜您中奖了！' if num==654321 else '您本期未中大奖！'
print(result)

print('*'*60)
print('恭喜您中奖了！' if num==654321 else '您本期未中大奖！')