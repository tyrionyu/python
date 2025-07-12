num = [1, 2, 3]
num.append([4, 5])
print(num)

result = [1, 2, 3]
result.extend([4, 5])
print(result)

n = [1, 2, 3]
for i in [4, 5]:
    n.append(i)
print(n)
