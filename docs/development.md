# Development

First, clone the repository and `cd` into it: `git clone git@github.com:Kiro47/MTU-Transfer-Course-Gatherer.git && cd MTU-Transfer-Course-Gatherer`.

Then:

## With Docker

**Prerequisites**: Docker

1. Build the container: `docker build -t mtu-courses --file Dockerfile.dev .`
2. Open a shell in the container: `docker run --mount type=bind,source="$(pwd)",target=/app -e SECRET_KEY="YOURSECRETKEY" -p 8000:8000 -p 3000:3000 mtu-courses`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the environment: `source venv/bin/activate`
5. Install dependencies and seed the database with an inital scrape: `./scripts/bootstrap with-dependencies`
6. Start the server and bundler with `supervisord`

## Without Docker

**Prerequisites**: Node.js, Python 3

1. Create a virtual environment: `python3 -m venv venv`
2. Activate the environment: `source venv/bin/activate`
3. Create required environment variables for Django:
  - `EXPORT DJANGO_SETTINGS_MODULE="course_gather.settings.local_settings"`
  - `EXPORT SECRET_KEY="YOURSECRETKEY"`
4. Install dependencies and seed the database with an inital scrape: `./scripts/bootstrap with-dependencies`
5. Copy `webapp/.env.example` to `webapp/.env` and edit values if neccessary
6. Start the webapp bundler with `npm start` from inside the `webapp/` directory
5. Start the server with `python3 manage.py runserver`

## Scripts

- Scrape MTU and dump to `writer.csv`: `python3 banwebScrape.py`
- Make database migrations: `python3 manage.py makemigrations`
- Run database migrations: `python3 manage.py migrate`
- Import scraped data to database: `python3 manage.py custom_db_sync writer.csv`
