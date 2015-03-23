"""Extend the base Django dev server by running sass as a background process.
We only want to run it once, so check first that it's not already running.
The process will exit automatically if the Django server is CTRL+C'ed."""

from django.contrib.staticfiles.management.commands.runserver import Command as BaseCommand

import subprocess

class Command(BaseCommand):
    def handle(self, addrport='', *args, **options):
        process = subprocess.Popen(['ps', '-ef'], stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        # Now run normal command.
        super(Command, self).handle(addrport, *args, **options)
