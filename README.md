# Install Simple-CRUD-in-Django with new virtual environment


* Install Python 3.6.x
* Make virtual environment and execute following commands <br />
	```python -m venv simple-crud``` <br />
  ```cd simple-crud``` <br />
  ```source bin/activate``` <br />
* Place the **project** folder inside **simple-crud** <br />
  ```cd project```
* Install **requirements.txt** <br />
  ```pip install -r requirements.txt```
* Add <app name> in **settings.py** *INSTALLED_APP* block
* Execute following commands to create Database <br />
  ```python manage.py makemigrations``` <br />
  ```python manage.py migrate``` <br />
  ```python manage.py createsuperuser``` <br />
  ```python manage.py runserver``` <br />
* And you are done :)
