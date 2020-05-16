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

# Copy static site from webapp
COPY --from=webapp /app/static /app/static

WORKDIR /app

COPY . .

# Set environment variables
ARG DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

ARG SECRET_KEY
ENV SECRET_KEY=$SECRET_KEY

# Install Python dependencies
RUN pip3 install --upgrade pip -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["gunicorn", "-c", "course_gather/conf/gunicorn.ini", "course_gather.wsgi:application"]
