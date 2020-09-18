"Video club where you can watch a movie."
My site, LINK -  https://videoclubapp.herokuapp.com/

SETUP

1. Install Python 3.6 interpreter:
Addition information on https://www.python.org/downloads/

2. Create virtual environment for your project:
$ mkdir my_project && cd my_project
$ python –m venv name_your_venv
$ name_your_venv\Scripts\activate

3. Clone this repository into your directory my_project:
$ git clone https://github.com/kovrygakirill/videoClub
$ cd videoClub

4. Install requirements:
$ pip install -r requirements.txt

5. Create sendgrid account for system https://sendgrid.com/free/?source=sendgrid-python:
SendGrid is an add-on for providing scalable email delivery and analytics for apps.
This account will receive letters from registered users.
Settings can show in videoClub/settings.py
Create environment variables:
  'SENDGRID_USERNAME' : ,
  'SENDGRID_PASSWORD' : ,

6. Set email port:
if you use tls, set port 587.
Settings can show in videoClub/settings.py
Create environment variables:
  'EMAIL_PORT' : .

7. Plug PostgreSQL Data base(DB):
Settings can show in videoClub/settings.py
Create environment variables:
  'NAME': ,
  'USER': ,
  'PASSWORD': ,
  'HOST': ,
  'PORT': .

8. Set own domain name:
if you run server local, use 127.0.0.1:8000
Settings can show in videoClub/settings.py
Create environment variables:
   'DOMAIN_NAME' : .

9. Make migrations and run server:
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
