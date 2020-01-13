import pytest

from unit.Div import div
data1 = [ [4, 2, 2],
          [0, 3, 0],
          [1, 2, 0.5],
          [100000000, 1, 100000000],
          [-1, 2, -0.5],
          [2, -1, -2],
          [-9, -9, 1]
          ]

@pytest.mark.parametrize("num1,num2,expection",data1)
def test_div_int(num1, num2, expection):
    assert div(num1, num2) == expection

@pytest.mark.parametrize("num1,num2,expection", {
    (0.4, 2, 0.2),
    (10, 0.1, 100),
    (-1.5, 1, -1.5),
    (100000000, -2, -50000000),
})
def test_div_float(num1, num2, expection):
    assert div(num1, num2) == expection

@pytest.mark.parametrize("num1,num2,expection", [
    (1, "a", "error"),
    ("a", 2, "error"),
    ("a", "b", "error"),

])
def test_div_string(num1,num2,expection):
    assert div(num1, num2) == expection


# 测试异常情况,如除数为0
@pytest.mark.parametrize("num1,num2,expection", [
    (1, 0, "error")
])
def test_div_exception(num1, num2, expection):
    with pytest.raises(ZeroDivisionError):
        assert div(num1, num2) == expection
