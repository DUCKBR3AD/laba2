from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if months < 0:
        years -= 1
        months += 12
    if days < 0:
        months -= 1
        if months < 0:
            years -= 1
            months += 12
        days += 30 

    return years, months, days

def get_birth_date():
    while True:
        birth_date_str = input("Введите дату рождения в формате день/месяц/год: ")
        try:
            birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
            return birth_date
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, введите дату в формате день/месяц/год.")

def main():
    birth_date = get_birth_date()
    years, months, days = calculate_age(birth_date)
    print(f"Ваш возраст: {years} лет, {months} месяцев, {days} дней")

if __name__ == "__main__":
    main()
