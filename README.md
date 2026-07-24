# Web Application Automation Testing Suite

## Project Overview

The Web Application Automation Testing Suite is a Python-based automation testing project developed using Selenium WebDriver. The project automates the login functionality of the SauceDemo web application and validates user authentication without manual intervention.

This project demonstrates the use of Selenium for browser automation, automated testing, and web application validation.

---

## Features

- Automated browser launch
- Automatic navigation to the SauceDemo website
- Automated login using valid credentials
- Login validation
- Basic navigation testing
- Form validation testing
- Automatic browser closure after execution
- Console output showing test execution status

---

## Technologies Used

- Python 3
- Selenium WebDriver
- Google Chrome
- ChromeDriver
- Visual Studio Code
- Git & GitHub

---

## Project Structure

```
Web-Application-Automation-Testing-Suite/
│
├── browser_utils.py
├── test_login.py
├── test_navigation.py
├── test_validation.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Prerequisites

Before running the project, ensure the following software is installed:

- Python 3.x
- Google Chrome
- ChromeDriver (compatible with the installed Chrome version)
- Visual Studio Code (optional)
- Git

Install Selenium using:

```bash
pip install selenium
```

---

## Test Cases

### Login Test
- Opens the browser
- Navigates to SauceDemo
- Enters valid username and password
- Clicks the Login button
- Verifies successful login

### Navigation Test
- Opens a product page
- Returns to the inventory page
- Verifies successful navigation

### Validation Test
- Validates login form behavior
- Checks application responses for invalid or empty inputs

---

## How to Run

Run the following commands:

```bash
python test_login.py
```

```bash
python test_navigation.py
```

```bash
python test_validation.py
```

---

## Expected Output

- Chrome browser launches automatically.
- SauceDemo website opens.
- Login is performed automatically.
- Navigation and validation tests execute.
- Test results are displayed in the terminal.

Example:

```
✅ Login Test PASSED
✅ Navigation Test PASSED
✅ Validation Test PASSED
```

---

## Project Objective

The objective of this project is to automate web application testing using Selenium WebDriver. It reduces manual testing effort, improves testing efficiency, and verifies application functionality through automated test execution.

---

## Future Enhancements

- Add to Cart automation
- Remove from Cart automation
- Checkout automation
- Logout automation
- Screenshot capture for failed tests
- HTML test reports
- CI/CD integration using GitHub Actions

---

## Author

**Aarthi Alagumuthu**

Third Year Engineering Student

---

## License

This project is developed for educational and academic purposes.