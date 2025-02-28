
# -*- coding:utf -8 -*-
import numpy as np
from scipy.linalg import *

def convert_to_standard_form( A, b,c, var_bounds=None):
    m, n = A.shape

    # Step 1: 将不等式约束 Ax <= b 转化为 Ax + s = b
    A_new = np.hstack([A, np.eye(m)])  # 引入松弛变量 s
    c_new = np.hstack([c, np.zeros(m)])  # 目标函数没有松弛变量
    b_new = b  # b 不变

    # Step 2: 处理变量边界，将无界变量拆分为差值形式
    if var_bounds is not None:
        for i in range(n):
            lb, ub = var_bounds[i]
            if lb == -np.inf and ub == np.inf:  # 无界变量
                # 将 x_i = x_i^+ - x_i^-
                A_new = np.hstack([A_new[:, :i], A_new[:, i:i+1], -A_new[:, i:i+1], A_new[:, i+1:]])
                c_new = np.hstack([c_new[:i], c_new[i:i+1], -c_new[i:i+1], c_new[i+1:]])

    return A_new, b_new,c_new

