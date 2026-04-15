# OrangeHRM Selenium Framework

## Project Overview
This project is a beginner-friendly QA automation framework for OrangeHRM login testing.
It uses PyTest and Selenium WebDriver with a simple Page Object Model (POM) structure.

## Tech Stack
- Python
- Selenium WebDriver
- PyTest
- pytest-html
- Jenkins (Windows agent)

## Project Structure
```
orangehrm-selenium-framework/
│
├── tests/
│   └── test_login.py
│
├── pages/
│   └── login_page.py
│
├── reports/
│
├── requirements.txt
├── Jenkinsfile
├── README.md
```

## Local Run Instructions
1. Open a terminal in the project root.
2. Install dependencies:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
3. Run the test and generate HTML report:
   ```bash
   pytest -v tests --html=reports/report.html --self-contained-html
   ```
4. Open `reports/report.html` in your browser to view the test report.

## Jenkins CI/CD (Windows) Explanation
The pipeline in `Jenkinsfile` performs:
1. Environment checks for Python and pip.
2. Source checkout from SCM.
3. Dependency installation from `requirements.txt`.
4. Test execution with PyTest and HTML report generation in `reports/`.
5. Artifact archiving of `reports/**` so reports are available in Jenkins build outputs.

## Notes
- No hardcoded local paths are used.
- Run commands from the project root for both local and Jenkins runs.
- Make sure Microsoft Edge and a compatible Edge WebDriver are available on the test machine.
