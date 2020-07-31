def add(a,b):
    conclusion=a+b
    return conclusion
def subtract(a,b):
    conclusion=a-b
    return conclusion
def devide(a,b):
    conclusion=a/b
    return conclusion
def multiply(a,b):
    conclusion=a*b
    return conclusion
print('欢迎使用noob计算器')
a=float(input('输入第一个数'))
b=float(input('输入第二个数'))
c=int((input('如果用加法输入1，减法输入2，除法输入3，乘法输入4')))
if c==1:
    i=add(a,b)
    print(i)
elif c==2:
    i=subtract(a,b)
    print(i)
elif c==3:
    i=devide(a,b)
    print(i)
elif c==4:
    i =multiply(a,b)
    print(i)
else:
    print('输入错误')
