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
# For public resources
ENV PUBLIC_URL=/static

# We use ESLint 7.x, CRA uses 6.x. Gives warning unless this is set.
ENV SKIP_PREFLIGHT_CHECK=true

RUN npm run build

RUN mkdir -p /app/static/

RUN cp -r build/* /app/static

# Set up Django
FROM python:alpine

# Get PostgreSQL client
# https://stackoverflow.com/a/47871121
RUN apk update
RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual build-dependencies gcc musl-dev postgresql-dev

WORKDIR /app

COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --upgrade pip -r requirements.txt --no-cache-dir

# Remove unneeded build dependencies for smaller image
RUN apk del build-dependencies

# Set environment variables
ENV DJANGO_SETTINGS_MODULE="course_gather.settings.prod_settings"

# Copy source
COPY banwebScrape.py .
COPY course_gather ./course_gather
COPY manage.py .
COPY scraper ./scraper
COPY scripts ./scripts
# Copy static site from webapp
COPY --from=webapp /app/static /app/static-build

EXPOSE 8000
CMD ./scripts/startup
