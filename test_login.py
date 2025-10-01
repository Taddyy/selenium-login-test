import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# --- PHẦN CÀI ĐẶT ---
# Lấy đường dẫn tuyệt đối đến file HTML để script luôn chạy đúng
LOGIN_URL = "file://" + os.path.abspath("login.html")
driver = webdriver.Chrome()

# --- CÁC HÀM TIỆN ÍCH ---
def check_element_exists(by, value):
    """Kiểm tra xem một phần tử có tồn tại trên trang không."""
    try:
        driver.find_element(by, value)
    except NoSuchElementException:
        return False
    return True

# --- CÁC HÀM KIỂM THỬ ---

def test_1_successful_login():
    print("\nBắt đầu Test Case 1: Đăng nhập thành công...")
    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1) # Chờ trang xử lý
    assert check_element_exists(By.XPATH, "//h1[text()='Login Success!']")
    print("✅ Test Case 1: Thành công!")

def test_2_failed_login_wrong_info():
    print("Bắt đầu Test Case 2: Sai thông tin đăng nhập...")
    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    error_message = driver.find_element(By.ID, "error-message")
    assert error_message.is_displayed()
    print("✅ Test Case 2: Thành công!")

def test_3_failed_login_empty_fields():
    print("Bắt đầu Test Case 3: Bỏ trống trường thông tin...")
    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "username").send_keys("") # Bỏ trống
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    # Kiểm tra alert
    alert = driver.switch_to.alert
    assert "cannot be empty" in alert.text
    alert.accept() # Nhấn OK trên alert
    print("✅ Test Case 3: Thành công!")

def test_4_forgot_password_link():
    print("Bắt đầu Test Case 4: Link 'Forgot password?'...")
    driver.get(LOGIN_URL)
    forgot_link = driver.find_element(By.ID, "forgot-password")
    assert forgot_link.is_displayed() and forgot_link.is_enabled()
    print("✅ Test Case 4: Thành công!")

def test_5_signup_link():
    print("Bắt đầu Test Case 5: Link 'SIGN UP'...")
    driver.get(LOGIN_URL)
    signup_link = driver.find_element(By.ID, "signup")
    assert signup_link.is_displayed() and signup_link.is_enabled()
    print("✅ Test Case 5: Thành công!")

def test_6_social_login_buttons():
    print("Bắt đầu Test Case 6: Các nút Social Login...")
    driver.get(LOGIN_URL)
    facebook_btn = driver.find_element(By.CLASS_NAME, "facebook")
    twitter_btn = driver.find_element(By.CLASS_NAME, "twitter")
    google_btn = driver.find_element(By.CLASS_NAME, "google")
    
    assert facebook_btn.is_displayed()
    assert twitter_btn.is_displayed()
    assert google_btn.is_displayed()
    
    print("✅ Test Case 6: Thành công!")

# --- GỌI HÀM ĐỂ CHẠY TEST ---
if __name__ == "__main__":
    try:
        test_1_successful_login()
        test_2_failed_login_wrong_info()
        test_3_failed_login_empty_fields()
        test_4_forgot_password_link()
        test_5_signup_link()
        test_6_social_login_buttons()
        print("\n🎉 Tất cả các test case đã chạy thành công!")
    
    except AssertionError:
        print("\n❌ Có lỗi xảy ra trong quá trình test.")
    
    finally:
        time.sleep(2)
        driver.quit() # Đóng trình duyệt