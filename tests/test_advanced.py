# tests/test_advanced.py
import pytest
import requests
from src.data_fetcher import get_api_data

# Test này sử dụng fixture `calculator_instance` từ conftest.py
def test_calculator_class(calculator_instance):
    """Kiểm tra các phương thức của lớp Calculator."""
    print("Chạy test_calculator_class với fixture")
    assert calculator_instance.add(2, 3) == 5
    assert calculator_instance.subtract(10, 4) == 6
    assert calculator_instance.multiply(3, 3) == 9

@pytest.mark.skip(reason="Chức năng này đang được phát triển, bỏ qua test.")
def test_feature_in_development():
    """Test này sẽ bị bỏ qua."""
    assert False

@pytest.mark.xfail(reason="Phép tính này có lỗi với số thực, dự kiến thất bại.")
def test_expected_to_fail():
    """
    Test này được dự kiến là sẽ thất bại.
    Pytest sẽ ghi nhận là xfail (dự kiến thất bại) thay vì FAILED.
    """
    assert 0.1 + 0.2 == 0.3  # Phép toán này thất bại do sai số dấu phẩy động

@pytest.mark.slow
def test_slow_operation():
    """
    Một test chạy chậm được đánh dấu với marker 'slow'.
    Có thể lọc để chạy riêng các test này với `pytest -m slow`.
    """
    print("Chạy test chậm...")
    import time
    time.sleep(1)
    assert True

# --- Mocking Tests ---

def test_get_api_data_success(mocker):
    """
    Kiểm tra hàm get_api_data trong trường hợp API trả về thành công.
    `mocker` là một fixture từ plugin `pytest-mock`.
    """
    print("Chạy test mocking cho trường hợp thành công")
    # 1. Chuẩn bị một đối tượng giả (mock) cho response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": "dữ liệu giả lập thành công"}
    
    # 2. Patch (thay thế) hàm `requests.get` để nó trả về đối tượng giả của chúng ta
    mocker.patch('requests.get', return_value=mock_response)

    # 3. Gọi hàm cần test
    result = get_api_data("https://api.example.com/data")

    # 4. Kiểm tra kết quả
    assert result == {"data": "dữ liệu giả lập thành công"}

def test_get_api_data_failure(mocker):
    """
    Kiểm tra hàm get_api_data trong trường hợp API bị lỗi (ví dụ: timeout).
    """
    print("Chạy test mocking cho trường hợp thất bại")
    # 1. Patch hàm `requests.get` để nó ném ra một ngoại lệ
    mocker.patch(
        'requests.get',
        side_effect=requests.exceptions.Timeout("API bị timeout")
    )

    # 2. Gọi hàm cần test
    result = get_api_data("https://api.example.com/data")

    # 3. Kiểm tra xem hàm có xử lý lỗi và trả về đúng định dạng không
    assert "error" in result
    assert "API bị timeout" in result["error"]
