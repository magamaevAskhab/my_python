s="У лукоморья 123 дуб зеленый 456"
a=s.index("я")
b=s.count("у")
c=s.isalpha()
d= int(len(s))
print("Буква Я всречается :",a+1)
print("буква У встречается:", b)
if c == False:
    c=s.upper();
print ("Зажание 3 ",c)
if d>4:
    d=s.lower();
    print("Задание 4",d)
p = "O" + s[1:]
print("Задание 5: ",p)
