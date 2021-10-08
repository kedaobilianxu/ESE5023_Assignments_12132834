#5.2
import numpy as np
import matplotlib.pyplot as plt
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
X = []
for i in range(1,101):
    X.append(i)
Y = Total_solutions
plt.plot(X,Y)
max_solution = []
max_solution_ = max(Total_solutions)
for i in range(100):
    if Total_solutions[i] == max_solution_:
        max_solution.append(i)
min_solution = []
min_solution_ = min(Total_solutions)
for i in range(100):
    if Total_solutions[i] == min_solution_:
        min_solution.append(i)
print(max_solution)
print(min_solution)
plt.text(0 + 1, 26, 'Max_value[1,26]', color = 'g')
plt.text(44 + 1, 26, 'Max_value[45,26]', color = 'g' )
plt.text(87 + 1, 6, 'Min_value[88,6]', color = 'g')
plt.show()