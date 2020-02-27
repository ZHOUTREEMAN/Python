# 1.	掌握系统输入输出的基本方法
# 2.	掌握Python语言的数据类型、运算符、表达式等
# 3.	掌握基本的分支控制结构
func = int(input("选择功能：输入一个数值1(表示华氏温度转换为摄氏温度)或者2（表示摄氏温度转换为华式温度）"))
if func == 1:
    f = float(input())
    if f < -459.67:
        print("Error")
    else:
        print('%.2f' % ((f - 32) * 5 / 9))
elif func == 2:
    c = float(input())
    if c < -273.15:
        print("Error")
    else:
        print('%.2f' % ((c * 9 / 5) + 32))
else:
    print("Error")
