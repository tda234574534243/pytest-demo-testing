# tests/conftest.py
import sys
import os
import pytest

# === Fix lỗi import src ===
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT)
# ==========================

from src.calculator import Calculator

def pytest_configure(config):
    config.addinivalue_line("markers", "slow: đánh dấu test là chạy chậm")

@pytest.fixture(scope="module")
def calculator_instance():
    print("\n(Setup: Khởi tạo Calculator cho module)")
    instance = Calculator()
    yield instance
    print("\n(Teardown: Dọn dẹp sau khi tất cả các test trong module đã chạy)")
