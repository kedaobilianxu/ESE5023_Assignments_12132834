import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
Sig_Eqs = pd.read_table('earthquakes-2021-10-13_20-13-06_+0800.tsv')
Sig_Eqs_M = np.array(Sig_Eqs[['Year','Mag']])
num = len(Sig_Eqs_M)
Mag = []
for i in range(num):
    if(Sig_Eqs_M[i][1] > 6.0):
        Mag.append(int(Sig_Eqs_M[i][0]))
Mag_counter = Counter(Mag)
counter_mag_x = list(Mag_counter.keys())
counter_mag_y = list(Mag_counter.values())
plt.bar(counter_mag_x, counter_mag_y, ls='-', width=2, label='1.2', color='steelblue')
plt.legend()
plt.show()