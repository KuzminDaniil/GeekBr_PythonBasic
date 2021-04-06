list_number = 0
my_list = []
i = 1
while True:
    a = input(
        "Введите '1', чтобы добавить позицию \n Введите '2', чтобы посмотреть список \n Введите '3', чтобы посмотреть обработанный список \n Введите 'Stop' для выхода")
    if int(a) == 1:
        name = input("Введите название:")
        price = input("Введите цену:")
        volume = input("Введите количество:")
        measure = input("Введите единицы измерения")
        my_list.append((i, {"название": name, "цена": price, "количество": volume, "eд": measure}))
        i += 1
        print("\n")
    if int(a) == 2:
        print(my_list, "\n")
    if int(a) == 3:
        i = 0
        name = []
        price = []
        volume = []
        measure = []
        for a in my_list:
            name.append(my_list [i] [1] ['название'])
            price.append(my_list [i] [1] ['цена'])
            volume.append(my_list [i] [1] ['количество'])
            measure.append(my_list [i] [1] ['eд'])
        my_dict = {"название": name, "цена": price, "количество": volume, "eд": measure}
        for item in my_dict.items():
            print(item)
    if a == "Stop":
        break
