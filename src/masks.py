from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> Union[str]:
    '''возвращает скрытый номер карты'''
    str_card_number = str(card_number)
    if str_card_number == "":
        return "Пустая строка. Введите номер карты"
    if not str_card_number.isdigit():
        return "Введенные данные некорректны"

    if len(str_card_number) != 13 and len(str_card_number) != 16 and len(str_card_number) != 19:
        return "Номер введен неверно"
    if len(str_card_number) == 16:
        return f'{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}'
    elif len(str_card_number) == 13:
        return f'{str_card_number[:4]} {str_card_number[4]}**** {str_card_number[-4:]}'
    elif len(str_card_number) == 19:
        return f'{str_card_number[:4]} {str_card_number[4:6]}** **** *** {str_card_number[-4:]}'
    return ""


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    '''возвращает скрытый номер счета'''
    str_account_number = str(account_number)
    if len(str_account_number) != 20 or not str_account_number.isdigit():
        return 'Введенные данные некорректны'
    return f'**{str_account_number[-4:]}'
