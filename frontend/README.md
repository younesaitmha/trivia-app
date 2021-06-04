# Frontend - Trivia APP

## Getting Setup

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend).

## Installing Dependencies

1. **Installing Node and NPM**<br>
This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [here](https://nodejs.org/en/download/).

2. **Installing project dependencies**<br>
This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:
    ```bash
    npm install
    ```
    >_tip_: **npm i** is shorthand for **npm install**

# Required Tasks

## Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file.

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.

```bash
npm start
```

## Request Formatting

The frontend should be fairly straightforward and digestible. You'll primarily work within the ```components``` folder in order to understand, and if you so choose edit, the endpoints utilized by the components. While working on your backend request handling and response formatting, you can reference the frontend to view how it parses the responses.

After you complete your changes on the endpoints, ensure you return to the frontend to confirm your API handles requests and responses appropriately:

- Endpoints defined as expected by the frontend
- Response body provided as expected by the frontend

## Optional: Updating Endpoints and API behavior

Would you rather the API had different behavior - different endpoints, return the response body in a different format? Go for it! Make the updates to your API and the corresponding updates to the frontend so it works with your API seamlessly.

## Optional: Styling

In addition, you may want to customize and style the frontend by editing the CSS in the ```stylesheets``` folder.

## Optional: Game Play Mechanics

Currently, when a user plays the game they play up to five questions of the chosen category. If there are fewer than five questions in a category, the game will end when there are no more questions in that category.

You can optionally update this game play to increase the number of questions or whatever other game mechanics you decide. Make sure to specify the new mechanics of the game in the README of the repo you submit so the reviewers are aware that the behavior is correct.
