# TEMPLATE API REST PYTHON - FLASK

This project contains the template for API REST developed using Python with Flask framework and a PostgreSQL database.

## General dependences

- Python
- Flask
- PostgreSQL

## Environment variables

For a correct operation of the REST API it will be usefull to generate a .env file where to include the environment variables for service configuration. All these variables have default values to avoid errors at runtime.

There is an example file with the name .env.example where these variables are shown, as in the following:

```bash
# General
COMPOSE_PROJECT_NAME=datanext
ENVIRONMENT={production|development|testing}
DEBUG={True|False}

# Api
API_PORT=
SECRET_KEY=

# Database
DB_HOST=
DB_USER=
DB_PASSWORD=
DB_NAME=
```

- ENVIRONMENT: it allows you to indicate what configuration is loaded when API REST is started. The options can be **development**, **production** or **testing**.

- API_PORT: the port used to expose the service to others.

- SECRET_KEY: a secret value used to cypher Flask.

- Database section: those are self explanatory. Set DB_HOST to the container name of the database when running api as a devcontainer.

## Created Users

### Admin

```
user: admin@admin.com
pass: admin
```

## Setup

This section details the steps to follow for the correct installation of the API REST.

1. Create virtual environment:

```bash
$ python3 -m venv env
```

2. Activate environment:

```bash
$ source env/bin/activate
```

2. Upgrade pip:

```bash
$ pip install --upgrade pip
```

3. Install wheel:

```bash
$ pip install wheel
```

4. Install project dependencies for development:

```bash
$ pip install -r requirements/dev.txt
```

## Run

To launch the API REST, you just have to launch the following command:

```bash
$ python api.py
```

## Run tests

Unit tests are implemented for the defined endpoints. In order to launch these tests, the DB must be available and launch the following command:

```bash
$ pytest -v
```

## Coverage

To check the coverage of the tests performed, the following command must be executed:

```bash
$ coverage run -m pytest
$ coverage html
```

To see the coverage in a more elegant way we can execute the following command:

```bash
$ coverage html
```

An htmlcov directory will be generated. In it we can see an index.hml that contains the coverage of the project.

## Endpoint Example

```bash
$ curl http://localhost:5000/api/location/country?countries=Afghanistan,Albania&startYear=2005&years=2
$ curl http://localhost:5000/api/location/country?startYear=2005&years=10
$ curl http://localhost:5000/api/location/top?year=2020
$ curl http://localhost:5000/api/location/region?year=2020
```
