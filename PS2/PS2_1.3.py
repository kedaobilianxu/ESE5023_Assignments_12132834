import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
Sig_Eqs_0 = pd.read_table('earthquakes-2021-10-13_20-13-06_+0800.tsv')
Sig_Eqs_3_0 = np.array(Sig_Eqs_0[['Country','Mag']])
eq_country_choose = []
for i_count in range(len(Sig_Eqs_3_0)):
    if(Sig_Eqs_3_0[i_count][1] > 0):
        eq_country_choose.append(Sig_Eqs_3_0[i_count][0])
country_counter = Counter(eq_country_choose)
country = []
for keys,values in country_counter.items():
    country.append(keys)
def CountEq_LargestEq(country):
    Sig_Eqs = pd.read_table('earthquakes-2021-10-13_20-13-06_+0800.tsv')
    Sig_Eqs_3 = np.array(Sig_Eqs[['Year','Mo','Dy','Country','Mag']])
    eq_country = []
    for j in range(len(Sig_Eqs_3)):
        eq_country.append(Sig_Eqs_3[j][3])
    eq_times_counter = Counter(eq_country)
    print('the total number of earthquakes since 2150 B.C. of '+country +' is '+str(eq_times_counter[country]))
    num = len(Sig_Eqs_3)
    Mag_3 = []
    for i in range(num):
        if(Sig_Eqs_3[i][4] > 0):
            Mag_3.append(Sig_Eqs_3[i])
    num_3 = len(Mag_3)
    country_eq = []
    for i_eq_countr in range(num_3):
        if(Mag_3[i_eq_countr][3] == country):
            country_eq.append(Mag_3[i_eq_countr])
    len_country_eq = len(country_eq)
    country_eq_mag = []
    for i_max in range(len_country_eq):
        country_eq_mag.append(int(country_eq[i_max][4]))
    max_mag = max(country_eq_mag)
    max_mag_index = country_eq_mag.index(max_mag)
    max_eq_date = str(country_eq[max_mag_index][0])+'-'+str(country_eq[max_mag_index][1])+'-'+str(country_eq[max_mag_index][2])
    print('the date of the largest earthquake ever happened in '+country+' is '+max_eq_date)

len_country = len(country)
for i_out_put in range(len_country):
    CountEq_LargestEq(country[i_out_put])