import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

APP_URL = "http://app:5000"


def get_driver():
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    return webdriver.Chrome(options=opts)


def test_home_page_loads():
    """Test Case 1: Verify the home page loads and shows Flaskr heading"""
    driver = get_driver()
    try:
        driver.get(APP_URL)
        assert "Flaskr" in driver.page_source, "Flaskr heading not found on home page"
        print("PASS: Home page loaded successfully")
    finally:
        driver.quit()


def test_login_page_loads():
    """Test Case 2: Verify the login page loads and has login form"""
    driver = get_driver()
    try:
        driver.get(f"{APP_URL}/login")
        assert "Login" in driver.page_source, "Login text not found on login page"
        assert driver.find_element(By.NAME, "username"), "Username field not found"
        assert driver.find_element(By.NAME, "password"), "Password field not found"
        print("PASS: Login page loaded successfully")
    finally:
        driver.quit()