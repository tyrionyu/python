'''
根据父母身高预测儿子的身高
需求: 从键盘输入父母的身高，并使用eveal()或float()转换输入的数据类型，计算公式：儿子身高=（父母身高+母亲身高）*0.54
'''
fother=float(input('请输入爸爸的身高：'))
mother=float(input('请输入妈妈的身高：'))
print('预测儿子的身高为：',(fother+mother)*0.54)
