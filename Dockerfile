FROM hub.z.westeurope.blue-yonder.cloud/by/debian_9_jenkins:stable

# install sqlite3 package for the use of djangos db shell
RUN apt-get update
RUN apt-get install -y sqlite3 virtualenv vim

# install pip dependencies
ENV BY_DEV_INDEX https://software.z.westeurope.blue-yonder.cloud/for_dev/Debian_9/+simple/
RUN virtualenv -p python3.6 /tmp/venv

COPY . /leaderboard
WORKDIR /leaderboard

RUN /bin/bash -c 'source /tmp/venv/bin/activate && pip install -i $BY_DEV_INDEX -e .'

EXPOSE 8000

CMD /tmp/venv/bin/python leaderboard/manage.py collectstatic --noinput ;  /tmp/venv/bin/python leaderboard/manage.py makemigrations ; /tmp/venv/bin/python leaderboard/manage.py migrate ; /tmp/venv/bin/python leaderboard/manage.py runserver 0.0.0.0:8000