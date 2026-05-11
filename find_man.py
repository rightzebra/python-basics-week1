# 题目 3：通讯录查询程序（对应：独立完成通讯录查询）
# 题目要求
# 用字典做通讯录，键为姓名，值为手机号
# 实现功能：
# 可以添加新联系人
# 输入姓名，查询对应手机号
# 若姓名不存在，提示「无此联系人」
# 用循环做简易菜单，可重复查询 / 添加，输入 q 退出程序
# 考核知识点
# 字典增查、while 循环、条件判断、字符串输入处理

people={}
def new_friends():
    name=input("姓名：")
    if name in people:
        print("命名重复了")
    else:
        number=input("电话：")
        if not number:
            print("电话不能为空，添加失败")
            return
        people[name]=number
        print("添加成功")

def find_friend():
    name=input("姓名：")
    if name in people:
        print(f"{name}的电话号码是{people[name]}")
    else:
        print("「无此联系人」")

while True:
    x=input("请输入需要的操作,T为添加,C为查询,q为退出")
    if x.upper=="T":
        new_friends()
    elif x.upper=="C":
        find_friend()
    elif x=="q":
        break
    else:
        print("请输入指定操作")

