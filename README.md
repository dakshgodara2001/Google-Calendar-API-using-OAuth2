# Google Calendar Integration with Django

This project demonstrates how to integrate Google Calendar with a Django application using Google OAuth 2.0. It allows users to view events from their Google Calendar within the Django application.


## Setup

1. Clone the repository:

```bash
git clone https://github.com/dakshgodara2001/Google-Calendar-API-using-OAuth2.Git
```

2. Navigate to the project directory:

```bash
cd googleCalendarIntegration
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Apply the migrations:

```bash
python manage.py migrate
```

5. Run the server:

```bash
python manage.py runserver
```

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


