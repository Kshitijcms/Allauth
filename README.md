# Allauth — Django Authentication Project

A Django authentication project built with Django, django-allauth, Tailwind CSS v4, and DaisyUI.

## Features

- User Login and Signup
- Password Reset
- Change Password
- Remember Me
- User Dashboard
- User Profile
- Login History Tracking
- Logout Security
- Responsive UI with Tailwind CSS and DaisyUI

## Tech Stack

- Python
- Django
- django-allauth
- Tailwind CSS v4
- DaisyUI
- SQLite (local development)

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and configure `DJANGO_SECRET_KEY`.
5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Security

Keep `.env` and all secret keys out of version control.