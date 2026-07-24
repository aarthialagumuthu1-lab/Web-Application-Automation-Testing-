from browser_utils import create_driver, login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
def test_navigation():
    driver = create_driver(headless=True)
    try:
        login(driver)
        product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_name"))
        )
        product_name = product.text
        product.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "back-to-products"))
        )
        if product_name in driver.page_source:
            print("✅ Product Navigation Test PASSED")
        driver.find_element(By.ID, "back-to-products").click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("inventory")
        )
        print("✅ Back to Inventory Navigation Test PASSED")
    finally:
        driver.quit()
if __name__ == "__main__":
    test_navigation()