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

5. Set ypu Google account credentials for system:
This account is account system. This account will receive letters from registered users.
Settings can show in videoClub/settings.py
Create environment variables:
  'EMAIL_HOST_USER' : , 
  'EMAIL_HOST_PASSWORD' : .

6. Plug PostgreSQL Data base(DB):
Settings can show in videoClub/settings.py
Create environment variables:
  'NAME': ,
  'USER': ,
  'PASSWORD': ,
  'HOST': ,
  'PORT': .
  
7. Make migrations and run server:
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
