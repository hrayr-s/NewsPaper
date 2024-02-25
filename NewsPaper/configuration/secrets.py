from NewsPaper.venv import env


class SecretsConfig:
    SECRET_KEY = env('SECRET_KEY')
