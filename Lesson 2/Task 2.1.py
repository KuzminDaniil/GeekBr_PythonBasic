my_list = (2.322, False, 33, (1, 2), "str", 66, 77, {1, 2}, 88, (1,2))
choice = 0
while choice != 5:
    print("Выберете, чито вы хотите сделать")
    print("1. Посмотреть переменную my_list")
    print("2. Посмотреть тип переменной my_list")
    print("3. Посмотреть типы всех переменных в списке my_list")
    print("4. Посмотреть тип определенной переменной в списке my_list")
    print("5. Выход")
    choice = int(input("Введите число 1-5:"))
    print("")
    if choice == 1:
        print("Значение переменной my_list:", my_list)
    if choice == 2:
        print("Тип переменной my_list:", type(my_list))
    if choice == 3:
        for i in range(len(my_list)):
            print("Тип переменной №", i, "в списке my_list:", type(my_list[i]))
    if choice == 4:
        m = input("Введите номер переменной от 1 до", len(my_list),":")
        print("Тип переменной №", m, "в списке my_list:", type(my_list[m]))
    if choice == 5:
        break
    print("")