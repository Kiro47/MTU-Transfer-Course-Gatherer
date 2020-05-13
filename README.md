# Course Gatherer

The process to find out what classes are tranferable into MTU is an absolute
pain, so this tool was born.

## Setting up a dev environment

#### Clone the project

```
git clone git@github.com:Kiro47/MTU-Transfer-Course-Gatherer.git
```

#### CD into the cloned repository

```
cd MTU-Transfer-Course-Gatherer
```

#### Create a new python virtual environment for the project

```
python3 -m venv .
```

#### Activate the environment

```
source bin/activate
```

#### Install the required packages

```
pip install -r requirements.txt
```

#### Run the scrape script to collect the up to date course list

Note: This will likely take several minutes

This also automatically drops the output file to `/tmp/writer.csv`

```
./banwebScrape.py
```

#### Start the django project

This project uses [Django DRF](https://www.django-rest-framework.org/)


##### Make the database migrations

```
python3 manage.py makemigrations
```

##### Migrate the migrations to the databse
```
python3 manage.py migrate
```

##### Run the db sync sub command

```
python3 manage.py custom_db_sync /tmp/writer.csv
```

##### Run the django server

```
EXPORT DJANGO_SETTINGS_MODULE="course_gather.settings.dev_settings"
EXPORT SECRET_KEY="YOURSECRETKEY"
python3 manage.py runserver
```
