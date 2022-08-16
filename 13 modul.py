number_of_tickets = int(input("Введите число билетов:"))

total_amount = 0

for i in range(number_of_tickets):
    age = int(input(f"Введите возраст {i + 1}-го посетителя: "))
    if age < 18:
        continue
    elif 18 <= age <= 25:
        total_amount += 990
    else:
        total_amount += 1390
if number_of_tickets > 3:
    print("Сумма к оплате с учëтом скидки 10%: ", total_amount - total_amount / 100 * 10)
else:
    print("Сумма к оплате:", float(total_amount))