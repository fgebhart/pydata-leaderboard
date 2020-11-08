FROM hub.z.westeurope.blue-yonder.cloud/by/debian_9_jenkins:stable

ENV VIRTUAL_ENV /venv
ENV BY_DEV_INDEX https://software.z.westeurope.blue-yonder.cloud/for_dev/Debian_9/+simple/


# install sqlite3 package for the use of djangos db shell
RUN apt-get update
RUN apt-get install -y sqlite3 virtualenv vim

# must run as non-root user
RUN groupadd --gid 1001 john
RUN useradd --create-home --shell /bin/bash  --uid 1001 --gid 1001 john
RUN mkdir $VIRTUAL_ENV
RUN chown john /home/john
RUN chown john $VIRTUAL_ENV
USER 1001
WORKDIR /home/john

# first copy only requirements files to only invalidate the next setps in case of changed requirements
COPY requirements.txt /tmp/requirements.txt

# install pip dependencies



RUN virtualenv -p python3.6 $VIRTUAL_ENV
RUN /bin/bash -c 'source $VIRTUAL_ENV/bin/activate && pip install -i $BY_DEV_INDEX -r /tmp/requirements.txt'


COPY . /tmp/home
RUN cp -r /tmp/home/* $HOME/
RUN ls -lhrt /home/john


RUN /bin/bash -c 'source $VIRTUAL_ENV/bin/activate && pip install -i $BY_DEV_INDEX .'

EXPOSE 8080

ENTRYPOINT ["bash", "entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]