# Lab 03: Kiểm Thử Tự Động Form Đăng Nhập Bằng Selenium

Đây là dự án cho bài tập Lab 03 - Môn học Nhập môn Công nghệ Phần mềm.
Dự án này sử dụng **Python** và thư viện **Selenium** để viết một kịch bản kiểm thử tự động cho một form đăng nhập cơ bản, bao gồm các trường hợp thành công và thất bại.

## Chức năng kiểm thử 🧪
Kịch bản `test_login.py` bao gồm các trường hợp kiểm thử sau:
* Đăng nhập thành công với tài khoản hợp lệ (`admin`/`123456`).
* Đăng nhập thất bại với mật khẩu sai và kiểm tra thông báo lỗi.
* Hiển thị cảnh báo khi người dùng bỏ trống trường thông tin.
* Kiểm tra sự tồn tại và khả năng hoạt động của các đường link (`Forgot password?`, `SIGN UP`) và các nút bấm social.

## Hướng dẫn cài đặt 🛠️
Để chạy dự án này, bạn cần cài đặt các công cụ sau:

1.  **Python 3:** Tải về từ [python.org](https://www.python.org/).
2.  **Trình duyệt Google Chrome.**
3.  **Thư viện Selenium:** Mở terminal và chạy lệnh sau:
    ```bash
    pip install selenium
    ```
    *(Lưu ý: Selenium phiên bản mới sẽ tự động quản lý WebDriver tương ứng với phiên bản Chrome của bạn).*

## Cách chạy 🚀
1.  Clone repository này về máy tính của bạn.
2.  Mở terminal trong thư mục gốc của dự án.
3.  Chạy kịch bản kiểm thử bằng lệnh:
    ```bash
    python test_login.py
    ```
4.  Một cửa sổ trình duyệt Chrome sẽ tự động bật lên và thực hiện các bước kiểm thử. Kết quả sẽ được in ra trong cửa sổ terminal.