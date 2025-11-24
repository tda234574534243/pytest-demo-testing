# BÁO CÁO TÌM HIỂU VỀ PYTEST

**Đề tài:** Tìm hiểu về kiểm thử cho các ứng dụng Python với Pytest.

---

## 1. Giới thiệu

### 1.1. Kiểm thử phần mềm là gì?

Kiểm thử phần mềm (Software Testing) là quá trình đánh giá và xác minh một ứng dụng phần mềm để đảm bảo nó hoạt động đúng như mong đợi. Mục tiêu của kiểm thử là tìm ra lỗi, sai sót hoặc các yêu cầu còn thiếu so với yêu cầu thực tế. Đây là một giai đoạn không thể thiếu trong quy trình phát triển phần mềm để đảm bảo chất lượng sản phẩm.

### 1.2. Giới thiệu về Pytest

Pytest là một framework kiểm thử mã nguồn mở cho Python. Nó được thiết kế để giúp việc viết các bài kiểm thử (test case) trở nên đơn giản, dễ đọc và dễ mở rộng, từ các bài kiểm thử đơn giản cho đến các ứng dụng phức tạp.

**Tại sao chọn Pytest?**
*   **Cú pháp đơn giản:** Viết test chỉ với các hàm Python và từ khóa `assert`. Không cần phải học các cấu trúc phức tạp.
*   **Mạnh mẽ và linh hoạt:** Hỗ trợ fixtures để quản lý trạng thái và tài nguyên cho các bài kiểm thử.
*   **Tự động phát hiện test:** Tự động tìm các file `test_*.py` hoặc `*_test.py` và các hàm `test_*` bên trong chúng.
*   **Hệ sinh thái plugin phong phú:** Dễ dàng mở rộng với các plugin như `pytest-cov` (kiểm tra độ bao phủ), `pytest-django` (tích hợp Django), `pytest-mock` (hỗ trợ mocking).
*   **Thông tin lỗi chi tiết:** Khi một `assert` thất bại, pytest cung cấp thông tin chi tiết về các giá trị, giúp gỡ lỗi nhanh hơn.

## 2. Cài đặt

Để cài đặt `pytest` và các plugin phổ biến, ta sử dụng `pip`:

```bash
pip install pytest pytest-cov pytest-mock requests
```
*   `pytest`: Framework chính.
*   `pytest-cov`: Plugin để đo lường độ bao phủ của test (test coverage).
*   `pytest-mock`: Plugin tích hợp thư viện mock, giúp "giả lập" các đối tượng hoặc hàm.
*   `requests`: Thư viện để minh họa việc mock một API call.

## 3. Các khái niệm cốt lõi và Demo

### 3.1. Cấu trúc dự án Demo

Để dễ hình dung, chúng ta sẽ xây dựng một dự án nhỏ với cấu trúc như sau:

```
.
├── src/
│   ├── calculator.py       # Module chứa các hàm tính toán đơn giản
│   └── data_fetcher.py     # Module lấy dữ liệu từ một API giả
├── tests/
│   ├── conftest.py         # File cấu hình chung cho tests, chứa fixtures
│   ├── test_calculator.py  # Tests cho module calculator
│   └── test_advanced.py    # Tests cho các tính năng nâng cao
└── requirements.txt        # File chứa các thư viện cần thiết
```

### 3.2. Test case đầu tiên

Trong `pytest`, một test case đơn giản là một hàm có tên bắt đầu bằng `test_`.

**Ví dụ: `tests/test_calculator.py`**
```python
from src.calculator import add

def test_add():
    """Kiểm tra chức năng cộng hai số."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10
```
- Pytest sẽ tự động tìm và chạy hàm `test_add`.
- `assert` là từ khóa của Python, được `pytest` sử dụng để kiểm tra điều kiện. Nếu điều kiện sau `assert` là `False`, test case sẽ thất bại.

### 3.3. Fixtures - Quản lý tài nguyên

Fixtures là một trong những tính năng mạnh mẽ nhất của `pytest`. Chúng được dùng để cung cấp dữ liệu, thiết lập môi trường, hoặc khởi tạo các đối tượng cần thiết cho test.

Một fixture được định nghĩa bằng decorator `@pytest.fixture`.

**Ví dụ: `tests/conftest.py`**
```python
import pytest
from src.calculator import Calculator

@pytest.fixture
def calculator_instance():
    """Fixture để tạo một đối tượng Calculator."""
    print("\n(Setup: Khởi tạo Calculator)")
    instance = Calculator()
    yield instance
    print("\n(Teardown: Dọn dẹp sau khi dùng Calculator)")
```
- Mã trước `yield` là phần **setup** (chạy trước khi test cần nó).
- `yield` trả về đối tượng fixture.
- Mã sau `yield` là phần **teardown** (chạy sau khi test hoàn thành).

Để sử dụng fixture, chỉ cần truyền tên của nó như một tham số vào hàm test.

**Ví dụ: `tests/test_advanced.py`**
```python
def test_calculator_class(calculator_instance):
    """Kiểm tra lớp Calculator với fixture."""
    assert calculator_instance.add(2, 3) == 5
```

### 3.4. Parametrization - Chạy test với nhiều bộ dữ liệu

Decorator `@pytest.mark.parametrize` cho phép chạy cùng một test case với nhiều bộ dữ liệu khác nhau. Điều này giúp giảm lặp code và kiểm tra được nhiều trường hợp hơn.

**Ví dụ: `tests/test_calculator.py`**
```python
import pytest
from src.calculator import add

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (100, 200, 300),
    (0, 0, 0)
])
def test_add_parametrized(a, b, expected):
    """Kiểm tra hàm add với nhiều bộ dữ liệu."""
    assert add(a, b) == expected
```
Hàm `test_add_parametrized` sẽ được chạy 4 lần, mỗi lần với một bộ giá trị `(a, b, expected)` khác nhau.

### 3.5. Markers - Đánh dấu và lọc Tests

Markers cho phép bạn phân loại các test case. Điều này hữu ích khi bạn chỉ muốn chạy một nhóm test nhất định (ví dụ: chỉ chạy các test `slow`, hoặc bỏ qua các test `integration`).

- `@pytest.mark.skip`: Luôn bỏ qua test này.
- `@pytest.mark.xfail`: Đánh dấu test là "dự kiến sẽ thất bại". Nếu test thất bại, nó sẽ được tính là `XFAIL`, không phải `FAIL`.
- Custom markers: Bạn có thể tạo các marker tùy chỉnh.

**Ví dụ: `tests/test_advanced.py`**
```python
import pytest

@pytest.mark.skip(reason="Chức năng này chưa hoàn thiện")
def test_feature_in_development():
    assert False

@pytest.mark.xfail
def test_expected_to_fail():
    """Test này được dự đoán là sẽ thất bại."""
    assert 1 == 2

@pytest.mark.slow
def test_slow_operation():
    """Một test chạy chậm."""
    import time
    time.sleep(1)
    assert True
```
Để chạy các test được đánh dấu `slow`, dùng lệnh: `pytest -m slow`.

### 3.6. Kiểm thử ngoại lệ (Exception Testing)

Để kiểm tra xem một đoạn mã có ném ra ngoại lệ như mong đợi hay không, ta sử dụng `pytest.raises`.

**Ví dụ: `tests/test_calculator.py`**
```python
import pytest
from src.calculator import divide

def test_divide_by_zero():
    """Kiểm tra lỗi chia cho 0."""
    with pytest.raises(ValueError, match="Không thể chia cho 0"):
        divide(10, 0)
```
Test này sẽ thành công nếu `divide(10, 0)` ném ra một `ValueError` với thông báo chứa chuỗi "Không thể chia cho 0".

### 3.7. Mocking với `pytest-mock`

Mocking là kỹ thuật thay thế các phần của hệ thống (ví dụ: API calls, database connections) bằng các đối tượng giả (mocks) để cô lập test. Plugin `pytest-mock` cung cấp fixture `mocker`.

**Ví dụ: `tests/test_advanced.py`**
```python
from src.data_fetcher import get_api_data

def test_get_api_data_success(mocker):
    """Kiểm tra get_api_data khi API trả về thành công."""
    # Giả lập hàm requests.get trả về một đối tượng mock
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": "dữ liệu thành công"}
    
    mocker.patch('requests.get', return_value=mock_response)

    # Gọi hàm cần test
    result = get_api_data("https://api.example.com/data")

    # Kiểm tra kết quả
    assert result == {"data": "dữ liệu thành công"}
```
Ở đây, `mocker.patch('requests.get', ...)` đã thay thế hàm `requests.get` thật bằng một đối tượng giả, giúp test không phụ thuộc vào mạng và API bên ngoài.

## 4. Chạy Tests và Báo cáo

### 4.1. Chạy tất cả test
Mở terminal ở thư mục gốc của dự án và chạy lệnh:
```bash
pytest
```
Pytest sẽ tự động tìm và chạy tất cả các test. Để xem output chi tiết hơn (bao gồm cả output từ `print`), thêm cờ `-v` và `-s`:
```bash
pytest -v -s
```

### 4.2. Lọc test
- **Chạy các test được đánh dấu (marker):**
  ```bash
  pytest -m slow
  ```
- **Chạy test theo tên file hoặc tên hàm:**
  ```bash
  pytest tests/test_calculator.py
  pytest tests/test_calculator.py::test_add
  ```

### 4.3. Báo cáo độ bao phủ (Test Coverage)
Độ bao phủ cho biết tỷ lệ code của bạn được thực thi bởi các test case. Plugin `pytest-cov` giúp thực hiện việc này.
```bash
pytest --cov=src
```
Lệnh này sẽ chạy tất cả test và sau đó in ra một báo cáo về độ bao phủ cho các module trong thư mục `src`.

Để có báo cáo chi tiết dưới dạng HTML:
```bash
pytest --cov=src --cov-report=html
```
Một thư mục `htmlcov` sẽ được tạo. Mở file `index.html` trong đó để xem báo cáo trực quan.

## 5. Kết luận

Pytest là một công cụ cực kỳ mạnh mẽ và hiệu quả cho việc kiểm thử trong Python. Với cú pháp đơn giản, khả năng mở rộng qua plugin, và các tính năng nâng cao như fixtures và parametrization, nó giúp các nhà phát triển xây dựng các bộ test đáng tin cậy và dễ bảo trì. Việc áp dụng `pytest` vào dự án không chỉ giúp đảm bảo chất lượng phần mềm mà còn thúc đẩy một văn hóa phát triển tập trung vào chất lượng.
