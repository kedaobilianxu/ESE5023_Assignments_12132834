#2.1
import numpy as np
M1 = np.random.randint(0,51,size=(5,10))
M2 = np.random.randint(0,51,size=(10,5))#low,high,size
print(M1)
print(M2)
#2.2
def Matrix_multip(a,b):
    A = np.shape(a)
    B = np.shape(b)
    a_row = A[0]
    a_col = A[1]
    b_row = B[0]
    b_col = B[1]
    if(a_col!=b_row):
        print("can not mulitp!")
        exit
    else:
        pass
    result = np.zeros((a_row,b_col))
    for i in range(a_row):
        for j in range(b_col):
            mul_sum=0
            for t in range(a_col):
                mul_sum+=a[i][t]*b[t][j]
            result[i][j]=mul_sum
    print(result)

Matrix_multip(M1,M2)