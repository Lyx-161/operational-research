#!/user/bin/env python
# -*- coding:utf -8 -*-
import numpy as np

def initialize_feasible_solution(A,M,b,c):
    
    m,n=A.shape

    A_new = np.hstack([A, np.eye(m)])
    c_new = np.hstack([c, M*np.ones(m)])

    x=np.hstack([np.zeros(n),b])

    return A_new,b,c_new,x

'''A = np.array([[1,2,2],[2,1,2],[2,2,1]])
b = np.array([20,20,20])
c = np.array([-10,-12,-12])
M=1000
x = initialize_feasible_solution(A, M, b, c)
print("Initialized feasible solution:", x)'''

'''A = np.array([[1,-1],[-1,1]])
b = np.array([0,0])
c = np.array([-1,0])
M=1000
x = initialize_feasible_solution(A, M, b, c)
print("Initialized feasible solution:", x)'''