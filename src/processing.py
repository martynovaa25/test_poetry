def filter_by_state(list_input: List[Dict]): -> List[Dict]
'''функция сортировки по ключу'''
    new_list = []
    for dictionary in list_input:
        if i[state] == "EXECUTED":
            new_list.append(dictionary)
    return new_list


def sort_by_date(list_input: List[Dict], reverse = True): -> List[Dict]
'''функция сортировки по дате'''
    sorted_by_date = sorted(list_input, key = lambda x: x['date'], reverse = True)
    return sorted_by_date

