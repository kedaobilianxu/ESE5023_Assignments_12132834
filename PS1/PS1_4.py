#4
import numpy as np
def Least_moves(target_money,least_step=0):
        while(target_money%2==0):
            target_money = target_money / 2
            least_step += 1
        if(int(target_money) == 1):
            return least_step
        else:
            target_money = target_money - 1
            least_step += 1
            least_step = Least_moves(target_money, least_step)
            return least_step
        

num = np.random.randint(1,101,1)
print(str(num[0])+' RMB')
result = Least_moves(num[0])
print('least_moves = '+str(result))
