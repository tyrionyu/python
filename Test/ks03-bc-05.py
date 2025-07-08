total=0

for i in range(2,101,2):
    if i%3==0:
        continue
    total+=i
print(f'1-100不能被整除的偶数和是:{total}')