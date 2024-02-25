import os
import sys
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# get .env
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
)


def base_dir():
    return BASE_DIR


def get_allowed_hosts():
    hosts = env('ALLOWED_HOSTS')
    if ',' in hosts:
        return hosts.split(',')
    if ';' in hosts:
        return hosts.split(';')
    return [hosts]


def is_inside_test():
    return 'test' in sys.argv
