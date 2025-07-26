'''请综合使用while和continue，计算0~1000以内，所有偶数的和。'''
num=sum=0
while num<=1000:
    num+=1
    if num%2==1:
        continue
    sum+=num
print(sum)