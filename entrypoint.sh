# activate virtual env
source $VIRTUAL_ENV/bin/activate

# get postgres credentials from azure vault and set them as environment variables
python azure_credentials.py

# initialize django app
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
