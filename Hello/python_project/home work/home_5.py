

def day_week():
    
    status = False
    
    while status == False:
    
        try:
            day = int(input("Введите кол-во учебных дней за неделю: "))
            status = True
            if day <=7 and day > 0:
                return work_hous_week(day)
            else:
                print("Вы ввели неккоректное кол-во дней. Кол-во дней в неделю не может превышать 7 и не может быть меньше 0")
                day = int(input("Введите кол-во дней: "))
                day_week()
        except ValueError:
            print("Введите цифрами кол-во дней!")
    
    
def work_hous_week(day_week):
    
    hous_week = 0
    
    for i in range(1, day_week+1):
        status = True
        
        while status:
            try:
                hous = float(input(f'Введите кол-во часов для {i} дня учебы: '))
                if hous > 0 and hous <= 24:
                    hous_week += hous
                    status = False
                else:
                    print("Кол-во часов не может быть отрицательным числом и не может быть больше 24 часов, повтороите попытку ввода")
            except ValueError:
                print("Вы ввели не числовое значение, повторите попытку")
                
                
    return f'Ваше общее кол-во часов за неделю составляет {hous_week}'


print(day_week())
