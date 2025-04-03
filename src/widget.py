from src.masks import get_mask_card_number
from src.masks import get_mask_account
from datetime import datetime
import pytest


def mask_account_card(card_or_account: str) -> str:
    '''функция, которая принимает на вход номер карты или счета
    и маскирует их'''
    card_or_account_list = card_or_account.split()
    if not card_or_account_list:
        return "Данные введены некорректно"
    if 'Счет' in card_or_account:
        return f'Счет {get_mask_account(card_or_account_list[1])}'
    elif 'MasterCard' in card_or_account or 'Maestro' in card_or_account:
        return f'{card_or_account_list[0]} {get_mask_card_number(card_or_account_list[1])}'
    elif 'Visa' in card_or_account:
        card_name = []
        card_number = []
        for element in card_or_account_list:
            if element.isalpha():
                card_name.append(element)
            elif element.isdigit():
                card_number.append(element)
        str_card_number = "".join(card_number)
        if len(card_name) >= 2:
            return f'{card_name[0]}{card_name[1]} {get_mask_card_number(str_card_number)}'


@pytest.fixture
def card_data():
    return {
        "account": "Счет 12345678901234565678",
        "mastercard": "MasterCard 12345678901234565678",
        "visa": "Visa 12345678901234567890",
        "maestro": "Maestro 12345678901234563456"
    }


def get_date(my_date: str) -> str:
    """Функция конвертирования даты"""
    date_formats = ["%Y-%m-%dT%H:%M:%S.%f",
                    "%Y-%m-%dT%H:%M:%S",
                    "%Y-%m-%dT%H:%M",
                    "%Y-%m-%dT%H",
                    "%Y-%m-%d",
                    "%Y-%m",
                    "%Y",
                    "%H:%M:%S.%f",
                    "%M:%S.%f",
                    "%S.%f",
                    "%f"
                    ]
    for fmt in date_formats:
        try:
            date_obj = datetime.strptime(my_date, fmt)
            return date_obj.strftime("%d.%m.%Y")
        except ValueError:
            continue
    raise ValueError("Неверный формат даты")
