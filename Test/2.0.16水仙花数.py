num=[]

for i in range(100,1000):
    a=i//100        #百位数
    b=(i//10)%10    #十位数
    c=i%10          #个位数
    if a**3+b**3+c**3==i:
        num.append(i)
print(num)