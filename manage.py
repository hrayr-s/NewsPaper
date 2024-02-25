#!/usr/bin/env python

import os
import sys

# fix PyCharm tests
if sys.argv[0] and "django_test_manage.py" in sys.argv[0]:
    import configurations

    configurations.setup()

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
