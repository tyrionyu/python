a=1
b=0
def f1():
    print('--进入函数f1--')
    return True

(a>b) or f1()

#(a<b) or f1()   #--进入函数f1--

#(a>b) and f1()   #--进入函数f1--

#(a<b) and f1()