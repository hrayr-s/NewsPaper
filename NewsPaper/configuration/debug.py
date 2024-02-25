from NewsPaper.venv import env


class DebugConfig:
    DEBUG = env('DEBUG', cast=bool)
