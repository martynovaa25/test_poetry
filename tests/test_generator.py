import pytest
from generators import filter_by_currency
from generators import transaction_descriptions
from generators import card_number_generator
import re


@pytest.mark.parametrize("currency, expected_count",
[("USD", 3),
("RUB", 2)
])

def test_filter_by_currency(currency, expected_count):
    """Проверка на то, что количество отфильтрованных
    транзакций совпадает с ожидаемым, и что каждая транзакция имеет правильный код валюты"""
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == expected_count
    for transaction in result:
        assert transaction["operationAmount"]["currency"]["code"] == currency


transactions = [
    {
        "id": 1,
        "operationAmount": {
            "currency": {"code": "USD"}
        }
    },
    {
        "id": 2,
        "operationAmount": {
            "currency": {"code": "EUR"}
        }
    },
    {
        "id": 3,
        "operationAmount": {
            "amount": "1000"}  # Отсутствует ключ "currency"
    }
]


def test_filter_by_currency_missing_currency():
    """Проверка работы функции при отсутствии указания валюты"""
    usd_transactions = list(filter_by_currency(transactions, 'USD'))
    assert len(usd_transactions) == 1
    assert usd_transactions[0]['id'] == 1


def test_rise_filter_by_currency():
    """Проверка работы при транзакции без описания"""
    empty_transactions = []
    with pytest.raises(TypeError):
        filter_by_currency(empty_transactions, 'USD')


def test_rise_transaction_descriptions():
    """Проверка работы при транзакции без описания"""
    list_none = []
    with pytest.raises(ValueError):
        next(transaction_descriptions(list_none))


@pytest.mark.parametrize(
    "invalid_format",
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                },
            },
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                },
            },
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ],
)

def test_transaction_descriptions_invalid_format(invalid_format):
    """Проверка при неверном формате данных"""
    if list(invalid_format) and ("description" in i for i in invalid_format):
        with pytest.raises(KeyError):
            list(transaction_descriptions(invalid_format))


def test_transactions_description():
    transactions_for_test = [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на счет"}
    ]
    expected_descriptions = ["Перевод организации", "Перевод с карты на счет"]
    result = list(transaction_descriptions(transactions_for_test))
    assert result == expected_descriptions


@pytest.mark.parametrize("transactions_test , expected", [
    ([], []),  # пустой список
    ([{"description": "Перевод организации"}], ["Перевод организации"]),
    ([{"description": "Перевод с карты на счет"}, {"description": "Перевод организации"}], ["Перевод с карты на счет", "Перевод организации"])
])

def test_transaction_descriptions(transactions_test, expected):
    """Проверка при разных количествах записей и пустом списке"""
    result = list(transaction_descriptions(transactions_test))
    assert result == expected


def test_card_number_format():
    """Проверка на формат номера карты"""
    start, stop = 4000123456789010, 4000123456789015
    pattern = re.compile(r"\d{4} \d{4} \d{4} \d{4}")
    for card_number in card_number_generator(start, stop):
        assert pattern.match(card_number), f"Неверный формат: {card_number}"


def test_card_number_range():
    """Проверка на генерацию в заданном диапазоне"""
    start, stop = 4000123456789010, 4000123456789015
    for card_number in card_number_generator(start, stop):
        card_number_int = int(card_number.replace(' ', ''))
        assert start <= card_number_int <= stop, f"Номер вне диапазона: {card_number}"


def test_card_number_boundaries():
    start, stop = 4000123456789010, 4000123456789015
    generated_cards = list(card_number_generator(start, stop))
    """Проверяем, что первый и последний номера равны start и stop"""
    first_card = int(generated_cards[0].replace(' ', ''))
    last_card = int(generated_cards[-1].replace(' ', ''))

    assert first_card == start, f"Первый номер не равен start: {generated_cards[0]}"
    assert last_card == stop, f"Последний номер не равен stop: {generated_cards[-1]}"