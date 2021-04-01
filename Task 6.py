first_day_km = int(input("Введите предполгаемый километраж первого дня"))
target_km = int(input("Введите целевой километраж"))
i = 0
while target_km > first_day_km:
    i+=1
    first_day_km=first_day_km*1.1
print("Целевой километраж был достигнут на", i,"-ый день")
