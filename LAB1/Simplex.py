#!/user/bin/env python
# -*- coding:utf -8 -*-
import numpy as np

def bland_rule(c_N,N):
    for j in range(len(N)):
        if c_N[j]<0:
            return j
    return -1
    
def simplex(A,b,c,x):
    m,n=A.shape
    B=np.arange(n-m,n)
    N=np.arange(n-m)

    iteration=0
    flag=1
    while True:
        iteration+=1
        #print(f"Iteration {iteration}")

        B_matrix=A[:,B]
        #print(B_matrix)

        B_inverse=np.linalg.inv(B_matrix)
        c_B=c[B]
        lambda_T=c_B @ B_inverse

        r_cost=np.zeros(len(N))
        for i in range(len(N)):
            A_j=A[:,N[i]]
            r_cost[i]=c[N[i]]-lambda_T @ A_j

        if all(r >= 0 for r in r_cost):
            #print("Optimal solution found")
            break

        entering_index = bland_rule(r_cost, N)
        if entering_index == -1:
            flag=0
            optimal_value = c @ x
            return x, optimal_value,flag
        
        entering_variable=N[entering_index]
        #print(f"Entering variable:{entering_variable}")

        d_B=B_inverse @ A[:,entering_variable]
        #print(d_B)

        if all(d <= 0 for d in d_B):
            flag=-1
            #optimal_value = c @ x
            return x, 0,flag

        ratios=np.array([x[B[i]]/d_B[i] if d_B[i]>0 else np.inf for i in range(m)])
        #print(ratios)
        leaving_index = np.argmin(ratios)
        leaving_variable = B[leaving_index]
        #print(f"Leaving index: {leaving_index}")
        #print(f"Leaving variable: {leaving_variable}")

        x[entering_variable] = ratios[leaving_index]
        x[B] -= d_B * x[entering_variable]

        B[leaving_index] = entering_variable
        N[entering_index] = leaving_variable

        #print(f"Current solution: {x}")

    optimal_value = c @ x
    return x, optimal_value,flag

'''A = np.array([[1,2,2,1,0,0],[2,1,2,0,1,0],[2,2,1,0,0, 1]])
b = np.array([20,20,20])
c = np.array([-10,-12,-12,0,0,0])
x = np.zeros(A.shape[1])
x[A.shape[1]-b.shape[0]:] = b
solution,objectibe_function_value ,flag= simplex(A, b, c, x)
print("solution x:", solution)
print("Objiective function value:" ,objectibe_function_value)
print("Exit flag(1=solution found;-1=unbounded;0=no feasible solution):",flag)
'''

'''
A = np.array([[1,2,3],[2,4,6],[1,1,1]])
b = np.array([6,12,3])
c = np.array([1,2,3])
x = np.zeros(A.shape[1])
solution,objectibe_function_value ,flag= simplex(A, b, c, x)
print("solution x:", solution)
print("Objiective function value:" ,objectibe_function_value)
print("Exit flag(1=solution found;-1=unbounded;0=no feasible solution):",flag)
'''

'''
A = np.array([[1,0,0],[0,1,0],[0,0, 1],[1,0,1]])
b = np.array([2,2,2,2])
c = np.array([1,1,1])
x = np.zeros(A.shape[1])
print(x)
print(b)
x[A.shape[1]-b.shape[0]:] = b
solution,objectibe_function_value ,flag= simplex(A, b, c, x)
print("solution x:", solution)
print("Objiective function value:" ,objectibe_function_value)
print("Exit flag(1=solution found;-1=unbounded;0=no feasible solution):",flag)
'''

'''
A = np.array([[1,-1],[-1,1]])
b = np.array([0,0])
c = np.array([-1,0])
x = np.zeros(A.shape[1])
print(x)
print(b)
x[A.shape[1]-b.shape[0]:] = b
solution,objectibe_function_value ,flag= simplex(A, b, c, x)
print("solution x:", solution)
print("Objiective function value:" ,objectibe_function_value)
print("Exit flag(1=solution found;-1=unbounded;0=no feasible solution):",flag)
'''


'''A = np.array([[ 1, -1,  1]])
b = np.array([0])
c = np.array([-1,0,0])
x = np.zeros(A.shape[1])
print(x)
print(b)
x[A.shape[1]-b.shape[0]:] = b
solution,objectibe_function_value ,flag= simplex(A, b, c, x)
print("solution x:", solution)
print("Objiective function value:" ,objectibe_function_value)
print("Exit flag(1=solution found;-1=unbounded;0=no feasible solution):",flag)
'''