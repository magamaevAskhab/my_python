from random import randint
numbers = []
lst = [randint(-500,500) for i in range (1000)]
minn, maxx = lst.index(min(lst)), lst.index(max(lst)
if (minn > maxx):
    minn, maxx = maxx, minn
print(len([i for i in list [minn:maxx] if i <0]))
                                           
