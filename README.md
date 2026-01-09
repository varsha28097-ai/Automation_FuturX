FuturX Playwright Automation Framework

This project is an **end-to-end automation framework** built using **Playwright with Pytest**, following the **Page Object Model (POM)** design pattern.
It automates key navigations in the **FuturX application** with a stable, reusable, and scalable structure.


📌 Project Overview

* Automates FuturX web application
* Uses **persistent login (auth_state.json)** to avoid repeated authentication
* Designed with **real-world best practices**
* Suitable for **learning, interviews, and production-scale automation**



📁 Project Structure


futurx-playwright-automation/
│
├── pages/                 # Page Object Model (POM)
│   ├── base_page.py       # Common reusable methods & waits
│   ├── login_page.py      # Login & dashboard handling
│   ├── college_page.py    # College page navigation
│   ├── course_page.py     # Course page navigation
│   ├── search_page.py     # Search page navigation
│   └── profile_page.py    # Profile page navigation
│
├── tests/                 # Test cases
│   └── test_navigation.py # Dashboard → page navigation flow
│
├── save_login_state.py    # One-time login state generator
├── conftest.py            # Pytest fixtures & browser setup
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Project dependencies
├── .gitignore             # Ignored files (auth, cache, profiles)
└── README.md              # Project documentation

🧰 Tools & Technologies Used

| Tool                        | Purpose                    |
| --------------------------- | -------------------------- |
| **Python**                  | Programming language       |
| **Playwright**              | Browser automation         |
| **Pytest**                  | Test execution & reporting |
| **Page Object Model (POM)** | Clean test architecture    |
| **Git & GitHub**            | Version control            |
| **Chromium / Chrome**       | Browser execution          |



🧠 Page Object Model (POM) – Simple Explanation

What is POM?

Each web page is represented as a **separate Python class**.
Tests do not directly interact with UI elements — they use page methods.

Why POM?

* Cleaner tests
* Easy maintenance
* Reusable code
* Scales well for large applications

Example:

* `login_page.py` → handles login & dashboard readiness
* `college_page.py` → handles college page actions
* `course_page.py` → handles course page actions


🔐 Authentication Strategy (Important)

 Problem

FuturX uses **OAuth / Google login**, which should not be automated directly.

Solution

* Login **once manually**
* Save browser session into `auth_state.json`
* Reuse this session in all tests

This makes tests:

* Faster
* Stable
* OAuth-safe

🔑 One-Time Login Setup

Run this command **only once**:

```
python save_login_state.py
```

What happens:

1. Browser opens `dev.futurx.app`
2. Login manually (Google / Email)
3. After dashboard loads, press **ENTER** in terminal
4. `auth_state.json` is generated

> ⚠️ Do NOT commit `auth_state.json` to GitHub

▶️ How to Run Tests

Install Dependencies

```
pip install -r requirements.txt
playwright install
```

Run All Tests

```
pytest -v
```

Run a Specific Test File

```
pytest tests/test_navigation.py
```
 ⏱ Timeout & Stability Handling

* Global timeout configured **above 30 seconds**
* Navigation waits until **network is idle**
* No hard-coded sleeps inside test logic

This ensures:

* Stable dashboard navigation
* No flaky failures
* Reliable execution on slow networks

🔄 Automation Flow (Step-by-Step)

1. Project setup & dependency installation
2. Generate authentication state (one-time)
3. Launch tests using Pytest
4. Browser opens already logged in
5. Start from dashboard
6. Navigate to:

   * Colleges
   * Courses
   * Search
   * Profile
7. Validate page readiness

✅ Key Highlights

* Real-world OAuth handling
* Clean POM architecture
* Reusable & maintainable code
* Beginner-friendly yet industry-grade
* Ready for CI/CD extension

🚀 Possible Enhancements

* GitHub Actions CI
* Retry mechanism
* Screenshot on failure
* HTML / Allure reports
* Multi-user auth states

📌 Note

This framework is designed to reflect **professional automation practices** used in real software testing teams.

