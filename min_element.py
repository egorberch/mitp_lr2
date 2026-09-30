"""Задание № 9 (средней сложности): Минимальный элемент списка."""


def find_minimum(numbers):
    """Возвращает наименьший элемент из переданного списка чисел."""
    if not isinstance(numbers, list):
        raise TypeError("Аргумент должен быть списком.")
    if not numbers:
        raise ValueError("Список не должен быть пустым.")

    min_val = numbers[0]
    for item in numbers:
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise TypeError("Все элементы списка должны быть числами.")
        if item < min_val:
            min_val = item
    return min_val


def main():
    """Демонстрация поиска минимального элемента."""
    print("Результаты поиска минимального элемента:")
    test_lists = [
        [5, 2, 9, -3, 7],
        [42],
        [3.14, 2.71, -1.5, 0.0],
        [],
    ]
    for lst in test_lists:
        try:
            print(f"Список {lst} -> минимум: {find_minimum(lst)}")
        except (ValueError, TypeError) as err:
            print(f"Список {lst} -> Ошибка ({err})")


if __name__ == "__main__":
    main()
