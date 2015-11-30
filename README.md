# medagenda
calendar for doctors

Installation
============

To install:

	pip install -r requirements.txt
	python manage.py syncdb
	python manage.py migrate

To run:

	python manage.py runserver

Translation
===========

to generate .po files : 

	django-admin.py makemessages -l=en
	django-admin.py makemessages -l=fr
	django-admin.py makemessages -l=nl

for english, french and dutch.

complete translations and compile :

	django-admin compilemessages --locale=en
	django-admin compilemessages --locale=fr
	django-admin compilemessages --locale=nl


