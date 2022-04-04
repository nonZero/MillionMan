# 🤑💸🏦 Million Man 🏦💸🤑

*Just a sample django project.*

## Dev Setup

* Requirements:
    * [Python 3.9+](https://www.python.org/)
    * Poetry

* Clone the project:

      git clone https://github.com/nonZero/MillionMan.git

* Create a venv and install deps:

      poetry install

* Create DB:

      poetry run python manage.py migrate 

* Add some fake data:

      poetry run python manage.py create_fake_data 150

* Create a superuser for the admin site:

      poetry run python manage.py createsuperuser

* Run the development web server:

      poetry run python manage.py runserver


* Enjoy: <http://localhost:8000>


