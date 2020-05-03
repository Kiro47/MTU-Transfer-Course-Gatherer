FROM python:buster

RUN apt-get update
RUN apt-get -y install curl git rsync \
    # Node version 14
    && curl -sL https://deb.nodesource.com/setup_14.x | bash \
    && apt-get install nodejs


RUN git clone https://github.com/codetheweb/MTU-Transfer-Course-Gatherer.git /app/
WORKDIR /app/

# Install Python dependencies

RUN pip3 install --upgrade pip -r requirements.txt
RUN python3 ./manage.py makemigrations
RUN python3 ./manage.py migrate
RUN python3 ./banwebScrape.py
RUN python3 ./manage.py custom_db_sync /tmp/writer.csv

ARG DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

ARG REACT_APP_ENDPOINT
ENV REACT_APP_ENDPOINT=$REACT_APP_ENDPOINT

ARG PROD_KEY
ENV PROD_KEY=$PROD_KEY

WORKDIR /app/webapp/

RUN npm install --only=prod
RUN npm update
# Fix vulns
RUN npm audit fix
RUN npm run build
RUN mkdir -p /app/static/
RUN rsync -av --progress --exclude=static/ build/ /app/static/
RUN rsync -av --progress build/static/* /app/static/

WORKDIR /app/
EXPOSE 8000
CMD ["gunicorn", "-c", "course_gather/conf/gunicorn.ini", "course_gather.wsgi:application"]
