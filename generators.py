import pytest


@pytest.fixture
def empty_transactions():
    return []


def filter_by_currency(transaction, currency):
    """Функция, которая принимает на вход список словарей транзакций и валюту и находит
    из всего списка транзакцию с нужной валютой"""
    currency_code = list((x for x in transaction if x["operationAmount"]["currency"]["code"] == currency))
    for element in currency_code:
        yield element


def transaction_descriptions(transactions):
    """Генератор, на вход которого подается список словарей с транзакциями,
    на выходе - описание операции"""
    if not transactions:
        raise ValueError("Передано пустое значение!")

    for item in transactions:
        if "description" not in item:
            yield 'Отсутствует описание'
        else:
            yield item["description"]


def card_number_generator(start, stop):
    """Генератор, который возвращает номера банковских карт
    в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        formatted_card_number = " ".join([card_number[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_card_number
