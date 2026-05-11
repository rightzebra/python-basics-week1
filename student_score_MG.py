# 题目 2：学生成绩管理程序（对应：独立完成学生成绩管理）
# 题目要求
# 用列表嵌套字典存储多名学生信息：姓名、语文、数学、英语分数
# 封装 3 个简易函数：
# 添加学生信息
# 计算单个学生平均分
# 遍历打印所有学生成绩及平均分
# 手动录入 3 名学生数据，程序自动算出每个人平均分并格式化输出
# 考核知识点
# 列表 + 字典嵌套、函数定义与调用、数值计算、循环遍历

students = []
def append_inf(i):
    s=input(f"分别输入学生{i}的语文、数学、英语分数，用空格间隔: ")
    score=(s.split())
    yw=int(score[0])
    sx=int(score[1])
    yy=int(score[2])
    stu={"姓名":i, "语文":yw, "数学":sx,"英语":yy}
    avg_score(stu)
    students.append(stu)

def avg_score(i):
    avg=round((i["语文"]+i["数学"]+i["英语"])/3,1)
    i["平均分"]=avg

def print_score():
    for i in students:
        print(f"姓名：{i['姓名']} 语文：{i['语文']} 数学：{i['数学']} 英语：{i['英语']} 平均分：{i['平均分']}")

name=["小明","小李","小杨"]
for i in name:
    append_inf(i)

print_score()



