# -*- coding:utf-8 -*-

import numpy as np
import pre_work
import standrad_form
import Simplex
import daM
import generate_input
import time
import openpyxl

def check_full_rank(A,c):
    B=A.T
    Q,R=np.linalg.qr(B)
    dia=min(R.shape[0],R.shape[1])

    for i in range(dia):
        if R[i][i]!=0:
            continue
        else:
            R=np.delete(R,i,axis=0)
            R=np.delete(R,i,axis=1)
            Q=np.delete(Q,i,axis=1)
            c=np.delete(c,i,axis=0)
    
    A=(Q@R).T
    #A=np.round(A).astype(int)
    return A,c

if __name__=="__main__":
    # 示例问题

    wb = openpyxl.Workbook()
    ws = wb.active

    ws.title="Sample Sheet LP"
    ws.append(["n","time"])

    for LLL in range(5,10,5):
        #times=np.zeros(20)
        #edge=np.zeros(20)
        j=0
        while j<1:
            choose=5
            if choose==0:
                A = np.array([[1,2,2],[2,1,2],[2,2,1]])
                b = np.array([20,20,20])
                c = np.array([-10,-12,-12])

            elif choose==1:
                A = np.array([[1,-1],[-1,1]])
                b = np.array([0,0])
                c = np.array([-1,0])

            elif choose==2:
                A = np.array([[1,0,0],[0,1,0],[0,0, 1],[1,0,1]])
                b = np.array([2,2,2,2])
                c = np.array([1,1,1])
            
            elif choose==3:
                A = np.array([[1,2,3],[2,4,6],[1,1,1]])
                b = np.array([6,12,3])
                c = np.array([-1,-2,-3])

            elif choose==4:
                A=np.array([[1,1],[1,1/4],[1,-1],[-1/4,-1],[-1,-1],[-1,1]])
                b=np.array([2,1,2,1,-1,2])
                c=np.array([1,-1])

            else:
                n,m=generate_input.generate_random_input()
                A,b,c,target=generate_input.generate_matrix_and_vectors(n,m)
            
            print(A,b,'\n',c)
            starttime=time.time()
            M=np.max(c)*100
            epsilon=1e-10

            check,A1,b1=pre_work.pre_perform(A,b)
            #print(A1,b1)


            if check==False:
                print("LP has no feasible point")
                j-=1

            else:
                A2, b2, c2 = standrad_form.convert_to_standard_form(A1, b1, c)
                A2 ,c2= check_full_rank(A2,c2)
                #print(A2,b1,c)
                A3,b3,c3,x = daM.initialize_feasible_solution(A2, M, b2,c2)  
                #print(A3,b3,c3,x)
                #x=np.hstack([np.zeros(A.shape[1]),b1])
                solution,optimal_value,flag = Simplex.simplex(A3,b3,c3,x)
                solution[np.abs(solution)<epsilon] = 0
                endtime=time.time()
                times[j]=endtime-starttime
                if flag==-1:
                    print("unbounded")
                else:
                    print("solution:", solution)
                    print("optimal_value:", round(optimal_value,8))
                    print("time:",endtime-starttime)
            j+=1

        ws.append([n,times[0],times[1],times[2],
                   times[3],times[4],times[5],times[6],times[7],times[8],times[9]
                   ,times[10],times[11],times[12],
                   times[13],times[14],times[15],times[16],times[17],times[18],times[19]])
        
        #wb.save("sample.xlsx")
            
