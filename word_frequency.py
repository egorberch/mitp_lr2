"""Задание № 7 (повышенной сложности): Подсчет частоты слов в файле."""

import os
import re


def count_word_frequencies(filepath):
    """Считывает файл и возвращает словарь с частотой каждого слова."""
    if not isinstance(filepath, str):
        raise TypeError("Путь к файлу должен быть строкой.")
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"Файл '{filepath}' не найден.")

    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read().lower()

    words = re.findall(r"\b\w+\b", text)
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


def main():
    """Демонстрация подсчета частоты слов в файле."""
    print("Результаты анализа частоты слов:")
    test_files = ["sample.txt", "sample_missing.txt"]

    for path in test_files:
        try:
            result = count_word_frequencies(path)
            print(f"Файл '{path}':")
            for word, count in sorted(result.items()):
                print(f"  '{word}': {count}")
        except (FileNotFoundError, TypeError) as err:
            print(f"Файл '{path}': Ошибка ({err})")


if __name__ == "__main__":
    main()
