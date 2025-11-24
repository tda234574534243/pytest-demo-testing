# src/data_fetcher.py
import requests

def get_api_data(url):
    """
    Lấy dữ liệu từ một API.
    Trong một ứng dụng thực tế, hàm này có thể phức tạp hơn nhiều.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Ném lỗi nếu status code là 4xx hoặc 5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        # Trả về một cấu trúc lỗi chuẩn
        return {"error": str(e)}

