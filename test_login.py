from browser_utils import create_driver, login

def test_login():
    driver = create_driver(headless=False)

    try:
        login(driver)
        print("✅ Login Test PASSED")
        input("Press Enter to close the browser...")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()