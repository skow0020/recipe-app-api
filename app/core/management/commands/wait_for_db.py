"""
Django command to pause execution until database is available
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write('Waiting for database... you sly devilish bastard!')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write(
                    'Database unavailable, waiting 1 second...', Psycopg2OpError, OperationalError)
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
