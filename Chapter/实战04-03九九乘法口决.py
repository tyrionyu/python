'''
九九乘法口决
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{ j }X{ i }={i*j:<2}",end='  ')
    print()