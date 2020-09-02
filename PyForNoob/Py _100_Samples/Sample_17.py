# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# 程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。

import string
string = input('请输入字符：\n')
space = 0
others = 0
alpha = 0
i = 0
while i < len(string):
    n = string[i]
    if n.isalpha():
        alpha += 1
    if n.isspace():
        space += 1
    else:
        others += 1
    i += 1
print('char = %d,space = %d,others = %d'% (alpha,space,others))