#!/user/bin/env python
# -*- coding:utf-8 -*-
import numpy as np

def pre_perform(A,b):
    check1,A1,b1=check_zero_rows(A,b)
    A2=check_zero_columns(A1)
    check2,A3,b3=check_linear_dependence(A2,b1)
    if (check1 and check2):
        return True,A3,b3
    else :
        return False,A3,b3

def check_zero_rows(A,b):
    zero_rows=np.where(np.all(A==0,axis=1))[0]
    if zero_rows.size>0:
        #print(f'Zero rows found:{zero_rows}')
        A=np.delete(A,zero_rows,axis=0)
        b=np.delete(b,zero_rows,axis=0)
    return True,A,b
    
def check_zero_columns(A):
    zero_columns = np.where(np.all(A == 0, axis=0))[0]
    if zero_columns.size > 0:
        #print(f"Zero columns found: {zero_columns}")
        A=np.delete(A,zero_columns,axis=1)
    return A
    
def check_linear_dependence(A,b):
    i=0
    while i < A.shape[0]:
        j=i+1
        while j <A.shape[0]:
            #print(A,j)
            #print(A[j][0],A[i][0])
            lam=A[j][0]/A[i][0]
            for k in range(1,A.shape[1]):
                #print(i,j,k)
                if A[j][k]!=lam*A[i][k]:
                    break
                if k==A.shape[1]-1:
                    A=np.delete(A,j,axis=0)
                    j-=1
                    if b[j]==lam*b[i]:
                        b=np.delete(b,j,axis=0)
                    else:
                        return False,A,b
            j+=1
        i+=1
    return True,A,b


'''A = np.array([[1,2,3],[2,4,6],[1,1,1]])
b = np.array([6,12,3])
result = pre_perform(A, b)
print(result)'''