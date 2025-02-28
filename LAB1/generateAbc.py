# -*- coding:utf-8 -*-
import numpy as np
def generate(num_constraints,num_vars):
    # 随机生成目标函数系数
    c = np.random.randint(-10, 10, size=num_vars)

    # 随机生成约束矩阵 A 和右端项 b
    A = np.random.randint(-10, 10, size=(num_constraints, num_vars))
    b = np.random.randint(1, 20, size=num_constraints)
    return A,b,c