#!/usr/bin/env python
import os
import sys

# uncomment this line to use local versions of packages
# sys.path.insert(0, '/home/vagrant/dev/websites/django-cms-redirects')
# sys.path.insert(0, '/home/vagrant/dev/websites/pan-libs')

# ----------------------------------------------------------------------------

if __name__ == "__main__":

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wonderinwood.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'LiveSettings')

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
