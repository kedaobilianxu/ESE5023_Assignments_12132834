#5.2
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
 
Total_solutions = []
for j in range(1,101):
    solution = 0
    res = Find_expression(j)
    Total_solutions.append(len(res))
max_solution = max(Total_solutions)
max_solution_location = Total_solutions.index(max(Total_solutions))
print('拥有最多solution的数为：'+str(max_solution_location + 1)+', '+'solution数量为： '+str(max_solution))
min_solution = min(Total_solutions)
min_solution_location = Total_solutions.index(min(Total_solutions))
print('拥有最少solution的数为：'+str(min_solution_location + 1)+', '+'solution数量为： '+str(min_solution))