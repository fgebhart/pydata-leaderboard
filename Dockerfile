FROM hub.z.westeurope.blue-yonder.cloud/by/debian_9_jenkins:stable

# install sqlite3 package for the use of djangos db shell
RUN apt-get update
RUN apt-get install -y sqlite3 virtualenv vim

COPY requirements/requirements.txt /tmp/requirements.txt

# install pip dependencies
ENV VIRTUAL_ENV /tmp/venv
ENV BY_DEV_INDEX https://software.z.westeurope.blue-yonder.cloud/for_dev/Debian_9/+simple/
RUN virtualenv -p python3.6 $VIRTUAL_ENV

RUN /bin/bash -c 'source $VIRTUAL_ENV/bin/activate && pip install -i $BY_DEV_INDEX -r /tmp/requirements.txt'

COPY . /leaderboard
WORKDIR /leaderboard

# install package
RUN /bin/bash -c 'source $VIRTUAL_ENV/bin/activate && pip install -e .'

EXPOSE 8000

# initialize django app and manage credentials
ENTRYPOINT ["bash", "entrypoint.sh"]

# NOTE: ensure the environment variables ENDPOINT_USERNAME and ENDPOINT_PASSWORD are set

# run django app
CMD ["/tmp/venv/bin/python manage.py", "runserver", "0.0.0.0:8000"]
