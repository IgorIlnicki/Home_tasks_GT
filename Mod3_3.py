import re
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
"    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   "]
def normalize_phone(phone_number):
    p1=r"[\d\+]+"   # патерн для відбору знаку плюс і всіх цифр
    phone_number=''.join(re.findall(p1,phone_number)) # об'єднуєм всі елементи рядка в один
    if len(phone_number)==10:   # перевірка для довжині рядка на 10 елементів
        phone_number='+38'+phone_number # додоємо +38
    elif len(phone_number)==12:    # перевірка для довжині рядка на 12 елементів
        phone_number='+'+phone_number # додоємо +
    return phone_number


for phone in raw_numbers:
    print(normalize_phone(phone))
