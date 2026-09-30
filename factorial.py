"""Задание № 3 (средней сложности): Факториал числа."""


def calculate_factorial(n):
    """Возвращает факториал неотрицательного целого числа n."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Аргумент должен быть целым числом.")
    if n < 0:
        raise ValueError("Число должно быть неотрицательным.")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    """Демонстрация вычисления факториала."""
    print("Результаты вычисления факториала:")
    test_values = [0, 1, 3, -5, 7]
    for val in test_values:
        try:
            print(f"{val}! = {calculate_factorial(val)}")
        except (ValueError, TypeError) as err:
            print(f"{val}! = Ошибка ({err})")


if __name__ == "__main__":
    main()
