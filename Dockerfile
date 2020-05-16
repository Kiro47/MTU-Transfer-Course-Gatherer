# Build webapp
FROM node:alpine AS webapp

# Create webapp directory
RUN mkdir -p /app/webapp

WORKDIR /app/webapp

# Install packages
COPY webapp/package*.json ./

RUN npm ci --only=production

# Copy source
COPY webapp/src ./src
COPY webapp/public ./public

# Build app
ARG REACT_APP_ENDPOINT
ENV REACT_APP_ENDPOINT=$REACT_APP_ENDPOINT

RUN npm run build

RUN mkdir -p /app/static/

RUN cp -r build/* /app/static
RUN mv /app/static/static/* /app/static/
RUN rm -r /app/static/static

# Set up Django
FROM python:alpine

# Get PostgreSQL client
# https://stackoverflow.com/a/47871121
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

# Copy static site from webapp
COPY --from=webapp /app/static /app/static

WORKDIR /app

COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --upgrade pip -r requirements.txt --no-cache-dir

# Set environment variables
ENV DJANGO_SETTINGS_MODULE="course_gather.settings.prod_settings"

# Copy source
COPY . .

EXPOSE 8000
ENTRYPOINT ["gunicorn", "-c", "course_gather/conf/gunicorn.ini", "course_gather.wsgi:application"]
