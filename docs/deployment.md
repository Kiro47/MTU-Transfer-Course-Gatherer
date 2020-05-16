# Deployment

This application is built with Docker and requires a PostgreSQL database when deployed in a production environment.

An example Docker Compose stack is provided [here](docker-compose.yml).

You probably want to run `./bootstrap` after starting the application for the first time. With the sample Compose stack, the command to do so is `docker-compose exec backend ./bootstrap`.
