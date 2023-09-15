#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

# DONT TOUCH THIS FILE ______________________________________________________________

# Unlike Flask, Django doesnt require you to do any preemptive work to see your website
# Just run python manage.py runserver in the command prompt of its directory
# It will boot up a website locally at localhost:8000 or 127.0.0.1:8000 (either works)
# You can close it by typing Ctrl + C in the command prompt

# Applications and Routers
# You can link different applications onto one website, such as an about application, contact, login, homepage, etc.
# and really build the depth of the website.
# You can create a new application by typing python manage.py startapp in the command line
# This will run all the necessary setup for you without all the hassle