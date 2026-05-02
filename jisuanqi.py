firstNum=float(input("输入第一个数:"))
fuhao=input("输入运算符号:")
secondNum=float(input("输入第二个数:"))
s=0.0
match fuhao:
    case fuhao if fuhao=="+":
        s=firstNum+secondNum
    case fuhao if fuhao=="-":
        s=firstNum-secondNum
    case fuhao if fuhao== "*":
        s=firstNum * secondNum
    case fuhao if fuhao=="/":
        s=firstNum / secondNum

print("结果是：" , s)