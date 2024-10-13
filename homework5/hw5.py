def get_number():
    for num in range(30):
        if num % 2 != 0:
            yield num

def main():
    gen = get_number()
    numbers = list(gen)

    print("Первое значение:", numbers[0])
    print("Пятое значение:", numbers[4])
    print("Последнее значение:", numbers[-1])

if __name__ == "__main__":
    main()
