my_list = [7, 5, 3, 3, 2]
while True:
    add = input("Введите число или 'Stop' для выхода из программы:")
    if add == "Stop":
        break
    b = 0
    while True:
        counter = 0
        add = int(add)
        for i in my_list:
            if i < add:
                my_list.insert(counter, add)
                b = 1
                break
            if b == 1:
                break
            elif counter + 1 == len(my_list):
                my_list.append(add)
                b = 1
                break
            elif i > add and add > my_list[counter + 1]:
                my_list.insert(counter + 1, add)
                b = 1
                break
            counter += 1
        if b == 1:
            break
    print(my_list)
