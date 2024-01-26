import random

def get_numbers_ticket(min, max, quantity):
    lim = 0 
    for i in range(quantity): 
        numbers.add(random.randint(min, max))  #  додаємо до множини випадкове число
    if len(numbers) < quantity: # перевірка, чи були числа, що повторються і не включені до множини
            lim = quantity - len(numbers)  # визначаємо кількість чисел, що не ввійшли до множини
            get_numbers_ticket(min, max, lim)

numbers = set() # створюємо множину
min = input("Введіть мінімальне можливе число у наборі (не менше 1): \n")
if min.isdigit():
    min = int(min)
    if min > 0 and min < 1000: #  перевіряємо діапазон входження 
        print(f"min: {min}")
        good = True
    else: 
        print(f"Помилка вводу: min повинно лежати в межах від 1 до 1000 - у вас {min}")
        good = False
else:
    print(f"Помилка вводу: min повинно бути числом - ви ввели {min}")
    good = False

if good:
    max = input("Введіть максимальне можливе число у наборі (не більше 1000): \n")
    if max.isdigit():
        max = int(max)
        if min < max and max < 1001: #  перевіряємо діапазон входження 
            print(f"max: {max}")
            good = True
        else: 
            print(f"Помилка вводу: max повинно бути більше min і не більше 1000 - у вас {max}")
            good = False
    else:
        print(f"Помилка вводу: max повинно бути числом - ви ввели {max}")
        good = False

if good:
    quantity = input("Введіть кількість чисел, які потрібно вибрати (значення між min і max): \n")
    if quantity.isdigit():
        quantity = int(quantity)
        a = max - min 
        if quantity <= a: #  перевіряємо, чи quantity не більше допустимого числа чисел лотареї
            print(f"quantity: {quantity}")
            good = True
        elif quantity > max:
            print(f"Помилка вводу: quantity повинно бути меншим, ніж max - {quantity}")
            good = False
        else: 
            print(f"Помилка вводу: quantity повинно бути більшим, ніж різниця max та min - {quantity}")
            good = False
        
    else:
        print(f"Помилка вводу: quantity повинно бути числом - ви ввели {quantity}")
        good = False
    

if good: 
    get_numbers_ticket(min, max, quantity)
    
    numbers = sorted(numbers)   # сортуємо
    print(f"Набір унікальних випадкових чисел для лотерей = {numbers}")
else:
    print(f"Помилка вводу: Неправильне задання даних")
    numbers = numbers.clear()
    print(f"Набір унікальних випадкових чисел для лотерей = {numbers}")