import math

# 1.	熟悉并掌握Python语言的开发环境
# 2.	掌握Python语言的数据类型、运算符、表达式等知识点

# 整形表达式
print(2 * 3)
print(2 ** 3)
print(5 + 2 * 5)
print((5 + 2) * 5)

# 浮点型表达式
print(5.0 + 2.0)
print(9.0 * 0.5)
print(9.0 ** 0.5)

# 类型转化
print(float(4))
print(int(4))
print(int(5.3))
print(float(int(5.3)))

# 数学函数
print(math.ceil(5.3))
print(math.floor(8.6))
print(math.fabs(-100))
print(math.factorial(3))  # 阶乘
print(math.cos(math.pi / 2))

# math.cos(pi/2)的计算结果为什么不是0
# 因为Math.PI其实也只是PI的近似值，如果是PI的精确值的话，结果肯定是0了。
