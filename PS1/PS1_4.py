#4
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
        


result = Least_moves(5)
print(result)
