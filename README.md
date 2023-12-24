# Aviquo

v0.7.0

## Installation

### Clone the repo

```sh
git clone https://github.com/ProjectAviquo/aviquo.git
cd aviquo
```

### Before starting development, create a venv and install depenencies

```sh
python -m venv venv
pip install -r requirements.txt
```

### Prepare the database

```sh
cd aviquo
python manage.py makemigrations
python manage.py migrate
```

## Starting the server

### Create a superuser

```sh
python manage.py createsuperuser
 (enter info it prompts for)
```

### Run the server

```sh
./run.sh
```

### Open the server

Go to <https://localhost:8000/admin> and enter superuser info

Congratulations! You did it!
