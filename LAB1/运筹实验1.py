import numpy as np
#0.转换标准形式
def to_standard_form(c,A,b):
    m,n=A.shape
    A_standard=np.hstack([A,np.eye(m)])#添加松弛变量s
    c_standard=np.hstack([c,np.zeros(m)])#目标函数添加松弛变量的系数（0）
    return c_standard,A_standard,b

#1.检查A是否行满秩
def check_full_rank_qr(A,tol=1e-10):#检查满秩
    Q,R=np.linalg.qr(A)
    rank=np.sum(np.abs(np.diag(R))>tol)
    return rank==A.shape[0],rank
def remove_redundant_constraints(A,b,tol=1e-10):#移除冗余约束
    Q,R=np.linalg.qr(A)
    diag_R=np.abs(np.diag(R))
    rank=np.sum(diag_R>tol)
    A_reduced=A[:rank,:]
    b_reduced=b[:rank]
    return A_reduced,b_reduced

#2.初始可行基解
def initialize_big_m(c,A,b,M=1e5):
    m,n=A.shape
    artificial_vars=np.eye(m)#人工变量
    A_big_m=np.hstack((A,artificial_vars))
    c_big_m=np.hstack((c,-M*np.ones(m)))
    basic_solution=np.zeros(n+m)
    basic_solution[n:]=b
    return c_big_m,A_big_m,basic_solution

#3.单纯形法的迭代
def calculate_r_cost(c,B_inv,A,j):
    return c[j]-c[B_inv]@A[:,j]
def find_entering_variable(r_cost):
    return np.argmin(r_cost)
def find_leaving_variable(tableau):
    ratios=np.inf*np.ones(tableau.shape[0]-1)
    for i in range(1,tableau.shape[0]):
        if tableau[i,-1]>0:
            ratios[i,-1]=tableau[i,-1]/tableau[i,-1].min()
    return np.argmin(ratios)+1
def simplex(A,b,c):
    m,n=A.shape
    #构造单纯形表
    A=np.hstack((A,np.eye(m)))
    c=np.hstack((c,np.zeros(m)))
    tableau=np.hstack((A,b.reshape(-1,1)))
    #初始化基本变量索引
    basic_vars=np.arange(n,n+m)
    while True:
        r_cost=calculate_r_cost(c,basic_vars,A,basic_vars)
        if np.all(r_cost>=0):
            break
        entering_var_index=fin_entering_variable(r_cost)
        entering_var=basic_vars[entering_var_index]
        leaving_var=find_leaving_variable(tableau)
        basic_vars[leaving_var-1]=entering_var
        pivot=tablequ[leaving_var,entering_var]
        tableau[leaving_var]/=pivot
        for i in range(tableau.shape[0]):
            if i!=leaving_var:
                tableau[i]-=tableau[i,entering_var]*tableau[leaving_var]
        c-=c[entering_var]*tableau[leaving_var]
    optimal_solution=np.zeros(n+m)
    optimal_solution[basic_vars]=tableau[:,-1]
    return optimal_solution[:n],optimal_value

A=np.array([[1,2,2,1,0,0],[2,1,2,0,1,0],[2,2,1,0,0,1]])
b=np.array([20,20,20])
c=np.array([-10,-12,-12,0,0,0])
c_standard,A_standard,b_standard=to_standard_form(c,A,b)
is_full_rank,rank=check_full_rank_qr(A)
print("矩阵A是否满秩:",is_full_rank)
print("矩阵A的秩:",rank)
if not is_full_rank:
    A_reduced,b_reduced=remove_redundant_constraints(A,b)
    print("移除冗余约束后的矩阵A:\n",A_reduced)
    print("移除冗余约束后的向量n:\n",b_reduced)
else:
    print("矩阵A是满秩的,无需移除约束")
A_standard,b=remove_redundant_constraints(A_standard,b)
c_big_m,A_big_m,b=initialize_big_m(c_standard,A_standard,b)
print("扩展约束矩阵A:\n",A_big_m)
print("初始基本可行解:\n",b)
print("扩展目标函数系数c:\n",c_big_m)
optimal_solution,optimal_value=simplex(A_big_m,b,c_big_m)
print("最优解:",optimal_solution)
print("最优值:",optimal_value)