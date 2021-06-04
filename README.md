# Trivia App

## Introduction

Trivia App is a website built by a restful API, which permits you to create questions, see different categories and questions, and play a quiz to test your knowledge.<br>
`Game mechanism:` Currently, when a user plays the game they play up to five questions of the chosen category. If there are fewer than five questions in a category, the game will end when there are no more questions in that category.<br>
This FullStack project demonstrates my knowledge in building REST APIs with [Flask](https://flask.palletsprojects.com/en/2.0.x/).

## Starting the project

1. Clone the repository to your laptop.
2. From the backend directory, create a virtual environment, install requirements and set the required environment variables or check out the backend documentation [here]([backend/README.md](https://github.com/younesaitmha/trivia-app/blob/main/backend)).
3. Start the backend server by running ``` python run.py ```
4. Run another terminal session. In the frontend directory, run ``` npm install ``` to install the required dependencies.
5. Finally, start the frontend server by running ``` npm start ```
6. You can view the website by visiting or clicking [http://localhost:3000](http://localhost:3000) in your browser.

For more information about how to get up and running, consult the following documents:

- [Backend Documentation](https://github.com/younesaitmha/trivia-app/blob/main/backend)
- [Frontend Documentation](https://github.com/younesaitmha/trivia-app/blob/main/frontend)

## About the Stack

the backend is a server backed with Flask and SQLAlchemy. The frontend created using [react](https://reactjs.org/) and [jquery/ajax](https://api.jquery.com/category/ajax/). The two servers communicate using a REST api.

## How To Contribute?

- clone the project
- create a new branch
- open a pull request with only the changed files
- Suggestions
    1. Add an additional question field such as rating and make all corresponding updates (db, api endpoints, add question form, etc.)
    2. INTENSE: Add users to the DB and track their game scores
    3. Add capability to create new categories.
