from typing import List, Dict


def filter_by_state(list_input: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    '''функция сортировки по ключу'''
    new_list = []
    for dictionary in list_input:
        if dictionary.get('state') == state:
            new_list.append(dictionary)
    if not new_list:
        raise ValueError("Словарь с указанным статусом отсутствует")


def sort_by_date(list_input: List[Dict], reverse: bool = True) -> List[Dict]:
    '''функция сортировки по дате'''
    sorted_by_date = sorted(list_input, key=lambda x: x['date'], reverse=reverse)
    return sorted_by_date
