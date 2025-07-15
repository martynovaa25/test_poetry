from decorators import log
import pytest


def test_log():
    @log(filename='my_log.txt')
    def summa(x, y):
        return x+y
    result_summa = summa(1, 2)
    assert result_summa == 3

    def sb(x, y):
        return x - y
    result_sb = sb(2, 1)
    assert result_sb == 1

    def division_corr(x, y):
        return x / y
    result_division_corr = division_corr(4, 2)
    assert result_division_corr == 2

    def div_zero(x, y):
        return x / y
    with pytest.raises(ZeroDivisionError):
        div_zero(2, 0)


def test_my_func_error(capsys):
    @log()
    def my_func(x, y):
        return x / y

    my_func(2, 0)
    captured = capsys.readouterr()
    assert captured.out == 'my_func error: division by zero. Inputs:  (2, 0), {}\n\n'
