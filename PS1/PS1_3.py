#3
def Pascal_triangle(row_num):
    if row_num == 0:
        result = [[1]]
        exit
    if row_num == 1:
        result = [[1],[1,1]]
        exit
    result = [[1],[1,1]]
    row_num =  row_num -2
    row = 1
    while(row <= row_num):
        new_list = [1]
        ex_line = len(result[row])
        for i in range(ex_line-1):
            num = result[row][i]+result[row][i+1]
            new_list.append(num)
        new_list.append(1)
        result.append(new_list)
        row = row + 1
    print(result[row_num+1])

Pascal_triangle(100)
Pascal_triangle(200)
