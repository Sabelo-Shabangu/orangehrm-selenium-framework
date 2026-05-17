OrangeHRM Selenium Automation Framework
📌 Project Overview

This project is a Python-based QA Automation framework built using Selenium WebDriver and PyTest.
It follows the Page Object Model (POM) design pattern and supports data-driven testing using CSV files.

The framework is designed to be CI/CD ready with Jenkins and produces HTML test reports.

🛠 Tech Stack
Python 3
Selenium WebDriver
PyTest
pytest-html (reporting)
webdriver-manager
Jenkins (CI/CD)
CSV (test data)
📁 Project Structure
orangehrm-selenium-framework/
│
├── pages/               # Page Object Model classes
├── tests/               # Test cases (PyTest)
├── utils/               # Utility functions (CSV reader)
├── data/                # Test data (CSV files)
├── reports/             # HTML test reports (generated)
│
├── conftest.py          # Fixtures (driver setup, hooks)
├── pytest.ini           # PyTest configuration
├── Jenkinsfile          # CI/CD pipeline
├── requirements.txt     # Dependencies
└── .gitignore
