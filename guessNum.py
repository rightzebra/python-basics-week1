import random
def guessNum(p):
    while True:
        try:
            x=int(input("请输入你要猜的数字："))
            if(x>p):
                print("大了，再猜：")
            elif(x<p):
                print("小了，再猜：")
            else:
                break
        except ValueError:
            print("只能输入整数，请重新猜！")
        
    print("真棒！猜对了")
print("----猜数字小游戏现在开始----")
num=random.randint(1,1000)
guessNum(num)