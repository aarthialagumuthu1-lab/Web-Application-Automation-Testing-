from browser_utils import create_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_validation():
    driver = create_driver(headless=True)
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "login-button").click()
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3"))
        )
        if "Username is required" in error.text:
            print("✅ Empty Field Validation Test PASSED")
        else:
            print("❌ Empty Field Validation Test FAILED")
    finally:
        driver.quit()
if __name__ == "__main__":
    test_validation()