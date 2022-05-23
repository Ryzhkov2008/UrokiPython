# Задание
count_task = 0
count_hours = 0
call_wife = False
while count_hours < 8:
    count_hours += 1
    print(count_hours, "и час", sep = "")
    count_task += int(input("Сколько задач решает Максим? "))
    call = int(input("Звонит жена. Взять трубку? (1-да,0-нет)"))
    if call == "да":
       call_wife = True
print("Рабочий день закончился, задач выполнено", count_task)
if call_wife == True:
    print("нужно зайти в магазин")
