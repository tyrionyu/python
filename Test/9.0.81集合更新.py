'''
d = {
    'Alice': [45],
    'Bob': [60],
    'Candy': [75],
}
d['Alice']=[50,61,66]
d['Bob']=[80,61,66]
d['Candy']=[88,75,90]
print(d)
'''

d = dict()
d['Alice'] = []
d['Bob'] = []
d['Candy'] = []
d['Alice'].append(50)
d['Alice'].append(61)
d['Alice'].append(66)
d['Bob'].append(80)
d['Bob'].append(61)
d['Bob'].append(66)
d['Candy'].append(88)
d['Candy'].append(75)
d['Candy'].append(90)

print(d)