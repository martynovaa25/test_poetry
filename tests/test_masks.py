from src.masks import get_mask_card_number
from src.masks import get_mask_account


def test_get_mask_card_number():
    """Проверка правильности маскировки номера карты"""
    assert get_mask_card_number('1234567891011121') == '1234 56** **** 1121'
    assert get_mask_card_number('2345678910123') == '2345 6**** 0123'
    assert get_mask_card_number('4568952589035767850') == '4568 95** **** *** 7850'
    assert get_mask_card_number('') == 'Пустая строка. Введите номер карты'
    assert get_mask_card_number('123579643257953f') == 'Введенные данные некорректны'


def test_get_mask_account():
    """Проверка правильности маскировки номера счета"""
    assert get_mask_account('12345678910121314156') == '**4156'
    assert get_mask_account('123456890456789') == 'Введенные данные некорректны'
    assert get_mask_account('') == 'Введенные данные некорректны'
    assert get_mask_account('34698564fyihgr6538s') == 'Введенные данные некорректны'
