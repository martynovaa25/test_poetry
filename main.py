from typing import Union

'''получаем данные карты'''
card_number = input()
account_number = input()


def get_mask_card_number(card_number: Union[str, int]) -> Union[str]:
    '''возвращает скрытый номер карты'''
    length_number = 16
    str_card_number = str(card_number)
    if len(str_card_number) == length_number:
        return f'{str_card_number[:4]}, {str_card_number[4:6]}**, ****, {str_card_number[-4:]}'
    return ""


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    '''возвращает скрытый номер счета'''
    length_account = 20
    str_account_number = str(account_number)
    if len(str_account_number) == length_account:
        return f'**{str_account_number[-4:]}'
    return ""

