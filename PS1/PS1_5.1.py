#5.1
import numpy as np
def Find_expression(sum_num):
    plist = all_strings(9)
    result = []
    for command in plist:
        if eval(command) == sum_num:
            result.append(command + '=' + str(sum_num))
    return result
 
def all_strings(n):
    if n == 1:
        return ['1']
    result = []
    for s in all_strings(n - 1):
        result.append(s + str(n))
        result.append(s + "+" + str(n))
        result.append(s + '-' + str(n))
    return result
 

num = np.random.randint(1,101,1)
res = Find_expression(45)
for i in res:
    print(i)
print('Total counts: ', len(res))