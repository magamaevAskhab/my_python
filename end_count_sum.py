sum = 0
while True:
    x = input("Введите число: ")
    if x == "Стоп":
        break
    elif x.isdigit():  
        x = int(x)
        sum = sum + x
    else:
        print("Повторите ввод числа")
print("Сумма введённых чисел: ",sum)
