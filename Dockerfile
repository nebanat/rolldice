FROM python:2.7-slim
MAINTAINER Aaron Biliyok <abiliyok@gmail.com>

ENV INSTALL_PATH /rolldice
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:5000 --access-logfile - "rolldice.app:create_app()"
