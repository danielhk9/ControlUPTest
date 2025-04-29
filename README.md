# Airport API and Inventory UI Automation Tests

This project contains automated tests built for the exam assignment.

- **API tests** for AirportGap service
- **UI tests** for Inventory web application (Selenium-based)

The project uses **Python 3.10+**, **pytest**, **requests**, and **selenium**.


python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

install requirements:
pip install -r requirements.txt


To run api tests:
pytest api_tests/tests/ --log-cli-level=INFO -v 

To run e2e tests:
pytest e2e_tests/tests/ -v

### To run tests multiple times (repeat mode):

You can run a test multiple times using the --count option from pytest-repeat:
pytest e2e_tests/tests/test_inventory.py --count=20 -v


⚙️ Configuration
Project configuration (base URLs, credentials, API keys) is located in:
/api_tests/config.py
/e2e_tests/config.py





