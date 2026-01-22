"""Модуль для виджета банковских операций."""

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в строке.

    """
    # Разделяем строку на части
    parts = data.split()

    # Номер - последний элемент
    number = parts[-1]

    # Тип - все остальное
    account_type = " ".join(parts[:-1])

    # Проверяем что номер состоит из цифр
    if not number.isdigit():
        raise ValueError("Номер должен содержать только цифры")

    # Определяем карта или счет
    if len(number) == 16:
        masked_number = get_mask_card_number(int(number))
    else:
        masked_number = get_mask_account(int(number))

    return f"{account_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

    Пример: "2024-03-11T02:26:18.671407" → "11.03.2024"
    """
    # Разделяем по T и берем часть с датой
    date_part = date_string.split('T')[0]

    # Разделяем год, месяц, день
    year, month, day = date_part.split('-')

    # Формируем в нужном формате
    return f"{day}.{month}.{year}"