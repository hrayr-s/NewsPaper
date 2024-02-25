from django.db.models import TextChoices


class EnvChoices(TextChoices):
    development = 'development', "Development"
    production = 'production', "Production"
    staging = 'staging', "Staging"
    testing = 'testing', "Testing"
    local = 'local', "Local"
