from NewsPaper.base_conf import BaseConf
from NewsPaper.choices import EnvChoices
from NewsPaper.venv import env


class Local(BaseConf):
    ENVIRONMENT = EnvChoices.local
    DEBUG = True
    ALLOWED_HOSTS = ['*']


class Prod(BaseConf):
    ENVIRONMENT = EnvChoices.production
    DEBUG = False
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
