import pandas as pd
wind = pd.read_csv('C:\\Users\\Cao Zhe\\Desktop\\南科大课后作业\\环境编程\\PS2\\2281305.csv',engine='python')
wind_d_s = wind[['DATE','WND']]
wind_y_d = wind_d_s['DATE'].str.split('-',expand = True)
wind_s = wind_d_s['WND'].str.split(',',expand = True)
wind_merge = pd.merge(wind_y_d, wind_s, left_index=True, right_index=True)
wind_merge.drop(index = (wind_merge.loc[(wind_merge[3] == '9999')].index), inplace=True)
wind_merge.drop(index = (wind_merge.loc[(wind_merge[4] != '1')].index), inplace=True)
wind_merge[3] = wind_merge[3].str[2].astype(int)
wind_afterwash = wind_merge[['0_x','1_x',3]]
test = wind_merge.groupby(['0_x','1_x'],as_index=False).mean()
for i_out in range(len(test)):
    print(test['0_x'][i_out]+' - '+test['1_x'][i_out]+' 的平均风速为： '+str(test[3][i_out]))