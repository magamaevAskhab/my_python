import random
a = random.randint(1,100)
b = 0
i = 0
while (a != b) and (i < 5):
    b = int(input("Угадайте число: "))
    if b > a:
        print("Введённое вами число больше заданного, повторите попытку")
    elif a > b:
        print ("Введённое вами число меньше заданного, повторите попытку")
    else:
        print ("Поздравляю!")
    break
i += 1
print ("Простите конечно, но с вами что то не так")
