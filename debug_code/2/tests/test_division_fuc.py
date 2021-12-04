from My_funcs.solution import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [
    (10, 2, 5),
    (20, 10, 2),
    (30, -3, -10),
    (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result

@pytest.mark.parametrize("exepected_exception, devisionable, divider",[
    (ZeroDivisionError, 10, 0),
    (TypeError, 20, "2")
])
def test_division_with_error(exepected_exception, devisionable, divider):
    with pytest.raises(exepected_exception):
        division(devisionable, divider)

