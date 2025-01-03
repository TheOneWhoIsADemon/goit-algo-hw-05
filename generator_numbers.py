import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Знаходить всі дійсні числа у тексті та повертає їх як генератор.

    :param text: Текст для аналізу.
    :return: Генератор з числами.
    """
    # Знаходимо всі числа за допомогою регулярного виразу
    pattern = r'(?<!\S)-?\d+(\.\d+)?(?!\S)'
    matches = re.finditer(pattern, text)
    for match in matches:
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює суму всіх чисел у тексті, використовуючи переданий генератор.

    :param text: Текст для аналізу.
    :param func: Функція-генератор, яка знаходить числа у тексті.
    :return: Сума чисел.
    """
    return sum(func(text))

# Приклад використання
if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income:.2f}")
