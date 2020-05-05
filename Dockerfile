FROM node:buster AS builder

COPY . /app/

WORKDIR /app/webapp/

# Build up the frontend
ARG REACT_APP_ENDPOINT
ENV REACT_APP_ENDPOINT=$REACT_APP_ENDPOINT

RUN npm install --only=prod
RUN npm update
RUN npm run build
RUN mkdir -p /app/static/

RUN cp -r build/* /app/static
RUN mv /app/static/static/* /app/static/
RUN rm -r /app/static/static


FROM python:buster

# Copy contents from builder
COPY --from=builder /app /app

WORKDIR /app/

# Install python deps and build backend
RUN pip3 install --upgrade pip -r requirements.txt
RUN python3 ./manage.py makemigrations
RUN python3 ./manage.py migrate
RUN python3 ./banwebScrape.py
RUN python3 ./manage.py custom_db_sync /tmp/writer.csv

ARG DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

ARG SECRET_KEY
ENV SECRET_KEY=$SECRET_KEY

WORKDIR /app/
EXPOSE 8000
CMD ["gunicorn", "-c", "course_gather/conf/gunicorn.ini", "course_gather.wsgi:application"]
