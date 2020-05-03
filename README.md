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

This also automatically drops the output file to `transfer-info.csv` if no
arguments are supplied.

Find more argument info with `./banwebScrape.py --help`

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
python3 manage.py runserver
```

### TODOs
* Change the serializer to output in an object format
* Add filtering to the back end
* Make the react front end
