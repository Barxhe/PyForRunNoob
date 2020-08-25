# 题目：输入某年某月某日，判断这一天是这一年的第几天？

# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

myd =input('YYYY/MM/DD:')
print(type(myd))
months = (0,31,59,90,120,151,181,212,243,273,304,334)

myd =myd.split("/",-1)
year = int(myd[0])
month = int(myd[1])
day = int(myd[2])

if 0 < month <= 12:
    sum = months[month-1] + int(day)
    if (year % 4 ==0) and (myd > 2):
        sum  = months[month-1] + int(day)-1
    else:
        sum  = months[month-1] + int(day)
else:
    print('DATE ERROR')
print(sum)
