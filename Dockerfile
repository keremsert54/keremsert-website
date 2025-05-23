FROM python:3.11-slim
RUN apt-get update

RUN apt-get install libpq-dev -y
RUN apt-get install python3-dev build-essential -y
RUN apt-get install postgresql-client -y

ENV PYTHONDONTWRITEBYTECODE=1
ENV VIRTUAL_ENV=/opt/venv




RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY resume /srv/app
WORKDIR /srv/app
