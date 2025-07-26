L = ['Alice', 66, 'Bob', True, 'False', 100] 

num=0

for item in L:
    num+=1
    if num%2!=0:
        continue
    print(item)