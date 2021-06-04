# Trivia APP Backend

Trivia App is a website built by a restful API, which permits you to create questions, see different categories and questions, and play a quiz to test your knowledge.<br>
Game mechanism: Currently, when a user plays the game they play up to five questions of the chosen category. If there are fewer than five questions in a category, the game will end when there are no more questions in that category.<br>
This app project demonstrates my skills in building REST APIs with Flask.

## Table of Contents

- [Trivia APP Backend](#trivia-app-backend)
  - [Table of Contents](#table-of-contents)
  - [1. Getting Started](#1-getting-started)
    - [1.1. Installing Dependencies](#11-installing-dependencies)
      - [1.1.1. Python 3.8](#111-python-38)
      - [1.1.2. Virtual Environment](#112-virtual-environment)
      - [1.1.3. PIP Dependencies](#113-pip-dependencies)
      - [1.1.4. Project Key Dependencies](#114-project-key-dependencies)
  - [2. setting up](#2-setting-up)
    - [2.1. setting up the environment variables](#21-setting-up-the-environment-variables)
    - [2.2. Database Setup](#22-database-setup)
  - [3. Running the server](#3-running-the-server)
  - [4. Testing](#4-testing)
  - [5. API Reference](#5-api-reference)
    - [5.1. General](#51-general)
    - [5.2. error Handlers](#52-error-handlers)
    - [5.3. Endpoints](#53-endpoints)
      - [5.3.1. GET `/categories`](#531-get-categories)
      - [5.3.2. GET `/questions`](#532-get-questions)
      - [5.3.3. GET `/categories/<int:id>/questions`](#533-get-categoriesintidquestions)
      - [5.3.4. POST `/questions`](#534-post-questions)
      - [5.3.5. POST `/questions/search`](#535-post-questionssearch)
      - [5.3.6. POST `/quizzes`](#536-post-quizzes)
      - [5.3.7. DELETE `/questions/<int:id>`](#537-delete-questionsintid)

## 1. Getting Started

the code is following [pip8](https://www.python.org/dev/peps/pep-0008/)
```bash
├── trivia.psql  *** sql script to create database
├── run.py *** Instance of the app. to run is use `` python app.py ``
├── README.md
├── config.py *** Configurations file containing Database URLs, ... etc
├── models.py *** Contains SQLAlchemy models.
├── test_flaskr.py *** Containing unittest functions
├── requirements.txt *** The dependencies we need to install with `` pip3 install -r requirements.txt ``
├── .env *** create this file for the environment variables
└── flaskr
    └── __init__.py *** Contains routes and controllers
```

### 1.1. Installing Dependencies

#### 1.1.1. Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://www.python.org/downloads/)

#### 1.1.2. Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### 1.1.3. PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all the required packages we selected within the `requirements.txt` file.

#### 1.1.4. Project Key Dependencies

- [Flask](https://flask.palletsprojects.com/en/2.0.x/) is a lightweight backend micro-services framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM. You'll primarily work in `flaskr/__init__.py` and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) is the extension we'll use to handle cross origin requests from our frontend server.

## 2. setting up

Follow these setup instructions to get the project up and running

### 2.1. setting up the environment variables

Before running the project, you have to set in a `.env` file in the backend folder the environment variables below:

- `PROD_DATABASE_URI`, `DEV_DATABASE_URI`, and `TEST_DATABASE_URI`: Set the database URIs for SQLAlchemy for the different configuration classes.
- `SECRET_KEY`: set the secret key for the configuration classes
- `API_ENV`: set each configuration class you want the app to run on it

```bash
# Production DB URI
PROD_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/trivia'
# development DB URI
DEV_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/trivia_dev'
# testing DB URI
TEST_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/trivia_test'
# the secret key
SECRET_KEY='+\xec\xaa\xddN)$\xdb"\xed\x9e\xcb\xc0\xe2\xab'
# specify if you wanna run the app on [development, testing, production]
API_ENV='development'
```

### 2.2. Database Setup

With Postgres running and our trivia database created, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
psql trivia_dev < trivia.psql
```

notice that I've used the `trivia_dev` database, as I want to run the app in the development environment. For more information, checkout the [PostgreSQL Docs](https://www.postgresql.org/docs/9.1/backup-dump.html)

## 3. Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python run.py
```

## 4. Testing

In this project we are using `unittest` to test all functionalities. Create a testing database and store the URI in the `TEST_DATABASE_URI` environment variable.
To run the tests, run

```bash
# if exists, drop the testing database and create it again
dropdb trivia_test
createdb trivia_test
# restore the trivia dump file to the testing database
psql trivia_test < trivia.psql
# finally, from the `backend` directory, run
python test_flaskr.py
```

## 5. API Reference

### 5.1. General

- Base URL: this app is hosted locally under the port 5000. The API base URL is `http://localhost:5000/api/v1.0`
- Authentication: this app doesn't require any authentication or API tokens.
- You must set the header: `Content-Type: application/json` with every request.

you can use [Postman](https://learning.postman.com/docs/publishing-your-api/documenting-your-api/), [Curl](https://curl.se/docs/manual.html) or the vscode extension [Thunter Client](https://rangav.medium.com/thunder-client-alternative-to-postman-68ee0c9486d6) to test manually this API.

### 5.2. error Handlers

if any errors occurred, the API will return a json object in the following format:

```bash
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```

The following errors will be reported:

- 400: `bad request`
- 404: `resource not found`
- 405: `method not allowed`
- 422: `unprocessible`
- 500: `internal server error`

### 5.3. Endpoints

#### 5.3.1. GET `/categories`

#### 5.3.2. GET `/questions`


#### 5.3.3. GET `/categories/<int:id>/questions`

#### 5.3.4. POST `/questions`


#### 5.3.5. POST `/questions/search`

#### 5.3.6. POST `/quizzes`

#### 5.3.7. DELETE `/questions/<int:id>`
