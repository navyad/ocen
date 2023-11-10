# ocen
OCEN Integration for Loan Loan Journey [APIs](https://ocen.dev/docs/loan_journey/auction_and_offer/)


### Setup Instructions

1. **Python Version**: Ensure you have Python >=3.6 installed on your system.

2. **Virtual Environment**:

   Create and activate a virtual environment with Python 3.6:

   ```bash
   python3.6 -m venv proj
   source proj/bin/activate
   ```

3. **Install Dependencies**:

   Install the project dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

4. **Running async worker**:
   
   ```bash
   celery -A ocen worker --loglevel=debug
   ```

5. **Running Loan agent and Lender instances**:
   
  ```bash
  python manage.py runserver 8000
  python manage.py runserver 80001
  ```
