# Find highest value from list 
import random

ls=[]
for i in range (5):
    num= random.randint(10, 50)
    ls.append(num)
   
print(ls)

# ls= [50, 19, 13, 15, 29]
maX_num=0
for n in ls:
    if n > maX_num:
        maX_num=n
print(maX_num)  

