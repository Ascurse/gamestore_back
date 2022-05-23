# Gamestore_backend
This is a backend for my gamestore project - https://github.com/Ascurse/gamestore_front
## Description
All games ('api/v1/games) have the following fields:
- name (Game title)
- image
- year (Released)
- description
- genre
- price
You can choose multiple genres for one game.
Genres should be created at 'api/v1/genres'

### Tech
- Python 3.7
- Django 2.2.19

### Setup project

Clone the repo:
```
git@github.com:Ascurse/gamestore_back.git
```

Go to root folder:
```
cd gamestore
```

Install requirements:
```
pip install -r requirements.txt
```

Make migrations:
```
python manage.py migrate
```

Create superuser:
```
python manage.py createsuperuser
```

Run server:
```
python manage.py runserver
```

Than go to django admin pannel and make game instances.
Now you're ready to work with frontend!