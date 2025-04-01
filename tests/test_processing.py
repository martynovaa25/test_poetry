from src.processing import filter_by_state, sort_by_date
import pytest


def test_filter_by_state_incorrect_input_data():
    """Проверка работы функции при отсутствии словарей с указанным статусом state в списке"""
    with pytest.raises(ValueError, match="Словарь с указанным статусом отсутствует"):
        filter_by_state(
            [
                {"id": 594226727, "state": "CLOSED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CLOSED", "date": "2018-10-14T08:21:33.419441"},
            ],
            state = "EXECUTED"
        )


@pytest.mark.parametrize("input_data, expected_output", [
    ([{'date': '2023-10-01'}, {'date': '2023-09-01'}], [{'date': '2023-10-01'}, {'date': '2023-09-01'}]),
    ([{'date': '2023-09-01'}, {'date': '2023-10-01'}], [{'date': '2023-10-01'}, {'date': '2023-09-01'}]),
    ([{'date': '2023-09-01'}, {'date': '2023-09-01'}], [{'date': '2023-09-01'}, {'date': '2023-09-01'}])
])
def test_sort_by_date(input_data, expected_output):
    """Функция проверяет удовлетворяет ли формат даты заданному"""
    assert sort_by_date(input_data) == expected_output
