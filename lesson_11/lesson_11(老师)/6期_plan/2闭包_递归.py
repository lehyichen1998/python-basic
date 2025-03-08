# 闭包阶乘 案例;

# 编写闭包函数实现 递归；
def recursion(num):
    # 基数条件
    if num == 1:
        return 1
    # 递归条件
    result = num * recursion(num - 1)
    return result


print(recursion(5))

# 实现过程

# ===> fact(5)
# ===> 5 * fact(5-1)
# ===> 5 * (4 * fact(5-1-1))
# ===> 5 * (4 * (3 * fact(5-1-1-1)))
# ===> 5 * (4 * (3 * (2 * fact(5-1-1-1-1))))

# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120

