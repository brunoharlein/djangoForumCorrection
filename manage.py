#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# un utilitaire en ligne de commande qui vous permet d’interagir avec
# ce projet Django de différentes façons. Vous trouverez toutes les
# informations nécessaires sur manage.py dans django-admin et manage.py.

import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forum.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
