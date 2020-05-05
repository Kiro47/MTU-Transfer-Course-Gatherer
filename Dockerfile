FROM node:buster AS builder

# Create webapp directory
RUN mkdir -p /app/webapp

# Copy JSX source files
COPY webapp/src /app/webapp/src
COPY webapp/public /app/webapp/public
COPY webapp/package*.json /app/webapp/

WORKDIR /app/webapp/

# Build up the frontend
ARG REACT_APP_ENDPOINT
ENV REACT_APP_ENDPOINT=$REACT_APP_ENDPOINT

RUN npm install --only=prod
RUN npm run build
RUN mkdir -p /app/static/

RUN cp -r build/* /app/static
RUN mv /app/static/static/* /app/static/
RUN rm -r /app/static/static


FROM python:buster

# Copy contents from builder
RUN ls -lR /app/
COPY --from=builder /app/static /app/static

# Copy base files
COPY banwebScrape.py /app/
COPY course_gather /app/course_gather
COPY manage.py /app/
COPY requirements.txt /app/
COPY run_tests /app/
COPY scraper /app/scraper

WORKDIR /app/

# Set environment variables
ARG DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

ARG SECRET_KEY
ENV SECRET_KEY=$SECRET_KEY

# Install python deps and build backend
RUN pip3 install --upgrade pip -r requirements.txt
RUN python3 ./manage.py makemigrations
RUN python3 ./manage.py migrate
RUN python3 ./banwebScrape.py
RUN python3 ./manage.py custom_db_sync /app/writer.csv

WORKDIR /app/
EXPOSE 8000
CMD ["gunicorn", "-c", "course_gather/conf/gunicorn.ini", "course_gather.wsgi:application"]
