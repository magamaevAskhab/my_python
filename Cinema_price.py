Film = input("Выберите фильм:")
Date = input("Выберите дату( сегодня,завтра): ")
Time = int(input("Выберите время:"))
Number = int(input("укажите количество билетов:"))

Film_Date={
    "Пятница":{12:250,16:350,20:450},
    "Чемпионы":{10:250,13:350,16:350},
    "Время сеанса":{10:350,14:450,18:450}
    }
price=Film_Date[Film]*[int(time)]
if Date=="завтра" and Number<20:
        Sale=0.95
elif Number>=20:
    Sale=0.80
else:
    Sale=1
print( price * sale)
    
