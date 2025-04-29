# AirportGap API and Inventory UI Automation Tests

This project contains automated tests built for the exam assignment.

- **API tests** for AirportGap service
- **UI tests** for Inventory web application (Selenium-based)

The project uses **Python 3.10+**, **pytest**, **requests**, and **selenium**.


python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

install requirements:
pip install -r requirements.txt


To run all api tests:
pytest api_tests/tests/ -v

To run all e2e tests:
pytest e2e_test/tests/ -v

To run a specific test file:
pytest e2e_test/tests/test_inventory.py -v
pytest api_tests/tests/test_airport.py -v

⚙️ Configuration
Project configuration (base URLs, credentials, API keys) is located in:
/api_tests/config.py
/e2e_test/config.py





