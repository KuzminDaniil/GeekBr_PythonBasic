my_string = input("Введите строку из нескольких слов:")
print("До разделения", my_string)
my_string = my_string.split(" ")
print("После разделения", my_string)
i = 0
while i < len(my_string):
    a = my_string [i]
    print(a [0:10])
    print(my_string [i] [0:10])
    i += 1
