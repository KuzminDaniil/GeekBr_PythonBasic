calc_type = input("Введите вид расчета: 'list' или 'dict':")
if calc_type == "dict":
    calendar = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}
    while True:
        month = input("Введите номер месяца или 'Stop' для выхода:")
        if month == "Stop":
            break
        print(calendar.get(int(month)))
if calc_type == "list":
    calendar = ("Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима")
    while True:
        month = input("Введите номер месяца или 'Stop' для выхода:")
        if month == "Stop":
            break
        print(calendar[int(month)])