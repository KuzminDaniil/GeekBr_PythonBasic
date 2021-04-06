income = float(input(print("Введите вашу выручку:")))
costs = float(input(print("Введите ваши издержки:")))
if income > costs:
    print(f"Вы в плюсе на {income-costs:.2f} ({(income/costs-1)*100:.0f}%)")
    profitability = income / costs
    staff = int(input(print("Введите численность вашей компании:")))
    print(f"Прибыль фирмы на одного сотрудника составляет {profitability/staff:.2f}")
elif income < costs:
    print(f"Вы в убытке на {costs-income:.2f} ({(income/costs-1)*100:.0f}%)")
elif income == costs:
    print("Вы вышли в 0")