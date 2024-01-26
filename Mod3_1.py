from datetime import datetime, timedelta
import re

def get_days_from_today(): 
    current_date = datetime.today()  # сьогоднішня дата
    print(f"Сьогоднішня дата: {current_date}")
    timedelta = current_date - some_date # визначаємо різницю між датами
    days = timedelta.days
    days = int(days) # переводимо у ціле
    print(f"Кількість днів: {days}")

some_date = input("Введіть дату у форматі РРРР-ММ-ДД: \n")

try:
    some_date = datetime.strptime(some_date, "%Y-%m-%d")
    print(f"Задана дата: {some_date}")  # задаємо дату
    get_days_from_today()
except Exception as error:  # якщо неправильно вказана дата
    print(f"Неправильно вказана дата: {error}")

