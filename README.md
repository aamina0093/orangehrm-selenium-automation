# OrangeHRM Selenium Automation Project

A selenium automation testing project built on the OrangeHRM demo website.
This project is built using Python, Pytest and Selenium to automate test cases
for the OrangeHRM HR Management application.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Pytest
- **Automation Tool:** Selenium WebDriver
- **Browser:** Google Chrome
- **Design Pattern:** Page Object Model (POM)

---

## 📁 Project Structure

```
orangehrm_automation/
│
├── tests/
│   ├── test_login.py        # Login & logout test cases
│   └── test_employee.py     # Employee module test cases
│
├── pages/
│   ├── login_page.py        # Page object for Login page
│   └── dashboard_page.py    # Page object for Dashboard page
│
├── conftest.py              # Pytest fixtures (browser setup/teardown)
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## ✅ Test Cases Covered

### Login Module
- Valid login with correct credentials
- Invalid login with wrong credentials
- Blank login (empty fields validation)
- Logout functionality

### Employee Module
- Navigate to Employee List
- Search employee by name
- Verify employee list has records

---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```
   git clone <your-repo-url>
   cd orangehrm_automation
   ```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Make sure Google Chrome is installed** on your system.
   Selenium 4 manages ChromeDriver automatically — no manual setup needed.

---

## ▶️ How to Run Tests

**Run all tests:**
```
pytest tests/
```

**Run a specific test file:**
```
pytest tests/test_login.py
```

**Run with detailed output:**
```
pytest tests/ -v
```

**Run and generate an HTML report:**
```
pytest tests/ -v --html=report.html
```

---

## 🌐 Website Under Test

**URL:** https://opensource-demo.orangehrmlive.com  
**Demo Credentials:**  
- Username: `Admin`  
- Password: `admin123`

---

## 👤 Author

Built as a learning project to practice Selenium automation testing.