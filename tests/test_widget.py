from src.widget import get_date, mask_account_card
import pytest


@pytest.mark.parametrize("input_crd, expected_mask", [
    ("Счет 12345678901234563456", "Счет **3456"),
    ("MasterCard 1234564890123456", "MasterCard 1234 56** **** 3456"),
    ("Visa Classic 1234456890123456", "VisaClassic 1234 45** **** 3456"),
    ("Maestro 1234567490123456", "Maestro 1234 56** **** 3456"),
])
def test_mask_account_card(input_crd, expected_mask):
    """функция проверяет работу маскировки номера карты или счета
        с предстоящим определением, что именно введено - карта или счет"""
    assert mask_account_card(input_crd) == expected_mask


@pytest.mark.parametrize("input_date, expected", [
        ("2023-10-05T14:30:00", "05.10.2023"),
        ("2023-10-05", "05.10.2023"),
        ("2023", "01.01.2023"),
])
def test_get_date(input_date, expected):
    """Функция проверки выходящего формата даты"""
    assert get_date(input_date) == expected
