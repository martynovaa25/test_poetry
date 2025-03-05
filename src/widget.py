from src.masks import get_mask_card_number
from src.masks import get_mask_account
from datetime import datetime

def mask_account_card(card_or_account: str) -> str:
    '''функция, которая принимает на вход номер карты или счета
    и маскирует их'''
    card_or_account_list = card_or_account.split()
    if 'Счет' in card_or_account:
        return f'Счет {get_mask_account(card_or_account_list[1])}'
    elif 'MasterCard' in card_or_account or 'Maestro' in card_or_account:
        return f'{card_or_account} {get_mask_card_number(card_or_account_list[1])}'
    elif 'Visa' in card_or_account:
        card_name=[]
        card_number=[]
        for element in card_or_account_list:
            if element.isalpha():
                card_name.append(element)
            elif element.isdigit():
                card_number.append(element)
        str_card_number = "".join(card_number)
        return f'{card_name[0]} {card_name[1]} {get_mask_card_number(str_card_number)}'

def get_date(my_date: str) -> str:
    '''функция отображения даты'''
    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")



