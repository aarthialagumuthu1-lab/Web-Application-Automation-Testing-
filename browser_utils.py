from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_driver(headless=False):
    options = Options()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Disable password popup
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    options.add_argument("--disable-save-password-bubble")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    return driver


def login(driver):
    driver.get("https://www.saucedemo.com/")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory")
    )