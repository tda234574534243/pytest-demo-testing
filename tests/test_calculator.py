# tests/test_calculator.py
import pytest
from src.calculator import add, divide, subtract, multiply

def test_add():
    """
    Kiểm tra chức năng cộng hai số.
    Đây là một test case đơn giản nhất.
    """
    print("Chạy test_add")
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),          # test case 1
    (-1, -1, -2),       # test case 2
    (100, 200, 300),    # test case 3
    (0, 0, 0),          # test case 4
])
def test_add_parametrized(a, b, expected):
    """
    Kiểm tra hàm add với nhiều bộ dữ liệu khác nhau
    sử dụng @pytest.mark.parametrize.
    """
    print(f"Chạy test tham số hóa: add({a}, {b}) == {expected}")
    assert add(a, b) == expected

def test_divide():
    """Kiểm tra chức năng chia."""
    print("Chạy test_divide")
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    """
    Kiểm tra việc ném ra ngoại lệ khi chia cho 0.
    Sử dụng context manager `pytest.raises`.
    """
    print("Chạy test_divide_by_zero")
    with pytest.raises(ValueError, match="Không thể chia cho 0"):
        divide(10, 0)

def test_add_tring():
    """Kiểm tra việc cộng chuỗi với chuỗi khác."""
    print("Chạy test_add_tring")    
    assert add("Hello, ", "World!") == "Hello, World!"
    assert add("","Test") == "Test"
    assert add("Py", "test") == "Pytest"
    assert add("123", "456") == "123456"
    assert add("!@#", "$%^") == "!@#$%^"