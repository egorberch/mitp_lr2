"""Задание № 5 (средней сложности): Список простых чисел до 100."""


def get_primes_up_to_100():
    """Возвращает список простых чисел в диапазоне от 2 до 100."""
    primes = []
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def main():
    """Демонстрация получения списка простых чисел."""
    print("Список простых чисел от 2 до 100:")
    primes = get_primes_up_to_100()
    print(primes)
    print(f"Всего простых чисел в диапазоне: {len(primes)}")


if __name__ == "__main__":
    main()
