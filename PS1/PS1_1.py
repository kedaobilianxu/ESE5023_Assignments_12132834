#1
def Print_values(a, b, c):
    if(a>b):
        if(b>c):
            print(str(a)+' , '+str(b)+' , '+str(c))
        else:
            if(a>c):
                print(str(a)+' , '+str(c)+' , '+str(b))
            else:
                print(str(c)+' , '+str(a)+' , '+str(b))
    else:
        if(b>c):
            if(a>c):
                print(str(a)+' , '+str(c)+' , '+str(b))
            else:
                print(str(c)+' , '+str(a)+' , '+str(b))
        else:
            print(str(c)+' , '+str(b)+' , '+str(a))
result_1 = Print_values(1,2,3)
result_2 = Print_values(3,2,1)
result_3 = Print_values(2,1,3)
print(result_1)
print(result_2)
print(result_3)