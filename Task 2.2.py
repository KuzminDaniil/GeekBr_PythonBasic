i = 0
my_list = list("")
while True:
    i += 1
    inp = input(print("Введите элемент", i, "списка my_list или 'Stop' для завершения ввода:"))
    if inp == "Stop":
        break
    my_list.append(inp)
print("")
print("Вы создали лист my_list:", my_list)
print("Список my_list состоит из", len(my_list), "элементов.")
print("")
print("Перемещаю элементы...")
print("")
i = 0
while i != len(my_list):
    if len(my_list) % 2 == 1:
        if i + 1 == len(my_list):
            break
    a = my_list[i]
    b = my_list[i + 1]
    my_list[i] = b
    my_list[i + 1] = a
    i += 2
print(my_list)
