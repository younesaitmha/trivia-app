from flaskr import create_app
from os import environ

# run the app with development configurations if the config isn't specified
config = environ.get('API_CONFIG') or 'development'

app = create_app(config)

# run the app
if __name__ == "__main__":
    app.run()
