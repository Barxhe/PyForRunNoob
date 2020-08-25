#题目：斐波那契数列。

#程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。



def fs(n):
    fs1 = 0
    fs2 = 1
    for i in range (n):
        fs1,fs2 = fs2,fs1+fs2
    print(fs1)

fs(10)