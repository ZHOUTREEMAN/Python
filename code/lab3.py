# 1. 掌握Python基本控制结构的使用方法
# 2. 熟悉多种控制结构的组合和嵌套使用
# 3. 考察使用Python解决数值求解问题的能力


# 1. 第一步，数字求和
# 如果列出10以内自然数中3或5的倍数，则包括3,5,6,9。那么这些数字的和为23。要求大家计算得出1000以内中3或5的倍数的自然数之和。
result = 0
for i in range(0, 1000):
    if (i % 3 == 0) | (i % 5 == 0):
        result = result + i
print(result)


# 2. 第二步，计算星期天
# 要求大家根据下列信息计算在1901年1月1日至2000年12月31日间共有多少个星期天落在每月的第一天上？
# a)  1900.1.1是星期一
# b)  1月，3月，5月，7月，8月，10月和12月是31天
# c)  4月，6月，9月和11月是30天
# d)  2月是28天，在闰年是29天
# e)  公元年数能被4整除且又不能被100整除是闰年
# f)  能直接被400整除也是闰年

def if_run(year):
    if (year % 4 == 0) & (year % 100 != 0):
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
