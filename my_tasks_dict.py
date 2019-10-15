from pprint import pprint
def add(a,b,c):
    a.append(input("Сформулируйте задачу: "))
    b.append(input("Добавьте категорию к задаче: "))
    c.append(input("Добавьте время к задаче: "))

def vivod(a,b,c):
    for i in range(len(x)):
        print("Задача: ", a[i])
        print("Категория: ", b[i])
        print("Дата: ", c[i])
a = []
b = []
c = []
while 0 == 0:
    print('Простой todo:\n1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.')
    k = int(input("Введите число: "))
    if k == 3:
        break
    dct = {1: add, 2: vivod}
    dct[k](a,b,c)
