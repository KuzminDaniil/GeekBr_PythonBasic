number = int(input(print("Введите число:")))
i = 10
ostatok = 0
max = 0
while (number*10 // i) != 0:
    if (number % i - ostatok)/i*10 > max:
        max = (number % i- ostatok)/i*10
    ostatok = number % i
    i = i * 10
print("Наибольшая цифра в числе -",int(max))
