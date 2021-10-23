import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
export_all = pd.read_csv('C:\\Users\\Cao Zhe\\Desktop\\南科大课后作业\\环境编程\\PS2\\Rice_China_export_Quantity.csv',engine='python')
export = export_all[['Partner Countries','Year Code','Value']]
export = np.array(export)
export_after_clean = []
for i_clean in range(len(export)):
    if(export[i_clean][2] > 0):
        export_after_clean.append(export[i_clean]) #洗数据
count_country = []
for i_count in range(len(export_after_clean)):
    count_country.append(int(export_after_clean[i_count][1]))
year_count = Counter(count_country) #统计每年的出口次数
print(year_count)
X = []
Y = []
for key,value in year_count.items():
    X.append(key)
    Y.append(value)
plt.bar(X, Y, label='3.2', color='steelblue')
plt.legend()
plt.show()
print(year_count[1987])
print(year_count[1993])
print(year_count[1995])
print(year_count[2000])
print(year_count[2003])
print(year_count[2005])
print(year_count[2008])
print(year_count[2013])
print(year_count[2015])