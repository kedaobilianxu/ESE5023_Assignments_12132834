import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
Sig_Eqs = pd.read_table('earthquakes-2021-10-13_20-13-06_+0800.tsv')
Sig_Eqs_A = np.array(Sig_Eqs[['Country','Deaths']])
C_D = []
row = len(Sig_Eqs_A)
k = 0
for i in range(row):
    if Sig_Eqs_A[i][1] > 0:
        C_D.append(Sig_Eqs_A[i])
C_D_dic = {}
for C_D_row in C_D:
    if C_D_row[0] in C_D_dic:
        C_D_dic[C_D_row[0]] += C_D_row[1]
    else:
        C_D_dic[C_D_row[0]] = C_D_row[1]
result = []
for (key,value) in C_D_dic.items():
    result.append([key,value])
result = sorted(result, key =(lambda x:x[1]), reverse = True)
print('top ten countries along with the total number of deaths')
for i in range(10):
    print(str(i+1)+'. country: '+str(result[i][0])+' death: '+str(result[i][1]))