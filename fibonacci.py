"""Задание № 3 (повышенной сложности): Сгенерировать список Фибоначчи."""


def generate_fibonacci(n):
    """Генерирует список первых n чисел последовательности Фибоначчи."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Аргумент должен быть целым числом.")
    if n < 0:
        raise ValueError("Количество элементов должно быть неотрицательным.")
    if n == 0:
        return []
    if n == 1:
        return [0]

    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


def main():
    """Демонстрация генерации списка чисел Фибоначчи."""
    print("Результаты генерации последовательности Фибоначчи:")
    test_values = [0, 1, 7, 10, -3]
    for count in test_values:
        try:
            res = generate_fibonacci(count)
            print(f"Первые {count} чисел: {res}")
        except (ValueError, TypeError) as err:
            print(f"Первые {count} чисел: Ошибка ({err})")


if __name__ == "__main__":
    main()
