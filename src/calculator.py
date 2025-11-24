# src/calculator.py

class Calculator:
    """Một lớp Calculator đơn giản."""
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Không thể chia cho 0")
        return a / b

# Các hàm riêng lẻ để minh họa các kiểu test khác nhau
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Không thể chia cho 0")
    return a / b
