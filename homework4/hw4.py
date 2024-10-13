import random

def find_multiples(x):
    numbers = [random.randint(0, 200) for _ in range(10)]
    multiples = list(filter(lambda num: num % x == 0, numbers))
    return numbers, multiples

def main():
    try:
        x = int(input("Введите число X: "))
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")
        return main()
    numbers, multiples = find_multiples(x)
    print(f"Сгенерированные числа: {numbers}")
    print(f"Числа, кратные {x}: {multiples}")
    return main()
if __name__ == "__main__":
    main()
