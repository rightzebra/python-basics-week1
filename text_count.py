# 题目 1：文本词频统计（对应：独立完成文本词频统计）
# 题目要求
# 定义一个函数 word_count(text)
# 传入一段英文字符串文本，做如下处理：
# 去除多余空格，按空格分割字符串
# 用字典统计每个单词出现的次数
# 最终返回词频字典，并遍历打印每个单词和对应次数
# 测试用文本："python java python c++ java python go"

def word_count(s):
    text=s.split()
    count_word={}
    for i in text:
        if i in count_word:
            count_word[i]+=1
        else :
            count_word[i]=1
    for x in count_word:
        print(f"{x}出现了{count_word[x]}次")

word="python java python c++ java python go"
word_count(word)
        