# Google Calendar Integration with Django

This project demonstrates how to integrate Google Calendar with a Django application using Google OAuth 2.0. It allows users to view events from their Google Calendar within the Django application.

## Requirements

- Python 3.6+
- Django 3.0+
- Django REST Framework
- Google Client Library

You can install these packages using pip:

\```
pip install django djangorestframework google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
\```

## Setup

1. Clone the repository:

\```bash
git clone https://github.com/your-github-username/your-repository.git
\```

2. Navigate to the project directory:

\```bash
cd your-repository
\```

3. Install the required packages:

\```bash
pip install -r requirements.txt
\```

4. Apply the migrations:

\```bash
python manage.py migrate
\```

5. Run the server:

\```bash
python manage.py runserver
\```

Your server will now be running at `http://127.0.0.1:8000/`.

## Google OAuth 2.0 setup

To use this project, you need to set up Google OAuth 2.0:

1. Follow the instructions in the [Python Quickstart Guide](https://developers.google.com/calendar/quickstart/python) to set up a Google OAuth 2.0 client.

2. Download the `credentials.json` file and rename it to `secret.json`.

3. Place the `secret.json` file in your project's base directory.

## How to use

1. Navigate to `http://127.0.0.1:8000/rest/v1/calendar/init/` to initiate the Google OAuth 2.0 process.

2. You will be redirected to Google. Log in with your Google account and grant the requested permissions.

3. You will then be redirected back to `http://127.0.0.1:8000/rest/v1/calendar/redirect/`, where you will see a list of events from your primary Google Calendar.

## Contributing

If you'd like to contribute to this project, please feel free to submit a pull request. For major changes, please open an issue first to discuss what you'd like to change.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.
