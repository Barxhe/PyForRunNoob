# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%;
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

# 程序分析：请利用数轴来分界，定位。


i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print (i-arr[idx])*rat[idx]
        i=arr[idx]
print(r)