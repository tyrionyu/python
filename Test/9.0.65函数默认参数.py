'''请定义一个 greet() 函数，它包含一个默认参数，如果没有传入参数，打印 Hello, world.，
如果传入参数，打印Hello, 传入的参数内容.'''

def greet(name='world'):
    print ('Hello, ' + name + '.')

# greet()
greet('Alice')