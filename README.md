# CRM Contact Management Project





A contanct Managment project  `Django 3.1` and `Python 3.2`.:

![djangorestframework](https://img.shields.io/pypi/djversions/djangorestframework?style=for-the-badge)  ![](https://img.shields.io/pypi/pyversions/Django?style=for-the-badge)


![App Screenshot](https://i.ibb.co/hdYJ871/Screenshot-53.png)

![App Screenshot](https://i.ibb.co/grpGQSB/Screenshot-54.png)

![App Screenshot](https://i.ibb.co/7tScw7r/Screenshot-55.png)

  
## SETUP

Run the following commands in Terminal:
```bash
./manage.py makemigrations
./manage.py migrate
```

**Attention: ** Before you using `./manage.py`, make sure the `python` command in your system is towards to `python 3.6` or above version. Otherwise you may solve this by one of the two following methods:
- Modify the first line in `manage.py`, change `#!/usr/bin/env python` to `#!/usr/bin/env python3`
- Just run with: `python3 ./manage.py makemigrations`
### Create super user

Run command in terminal:
```bash
./manage.py createsuperuser
```

### Create testing data
Run command in terminal:
```bash
./manage.py create_testdata
```

### Collect static files
Run command in terminal:
```bash
./manage.py collectstatic --noinput
./manage.py compress --force
```

### Getting start to run server
Execute: `./manage.py runserver`

Open up a browser and visit: http://127.0.0.1:8000/ , the you will see the Project.
