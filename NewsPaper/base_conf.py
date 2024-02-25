from configurations import Configuration

from NewsPaper.choices import EnvChoices
from NewsPaper.configuration.api import ApiConfig
from NewsPaper.configuration.business import BusinessConfig
from NewsPaper.configuration.debug import DebugConfig
from NewsPaper.configuration.django import DjangoConfig
from NewsPaper.configuration.frontend import FrontendConfig
from NewsPaper.configuration.locale import LocaleConfig
from NewsPaper.configuration.secrets import SecretsConfig
from NewsPaper.configuration.storage import StorageConfig


class BaseConf(
    ApiConfig,
    BusinessConfig,
    DebugConfig,
    DjangoConfig,
    FrontendConfig,
    LocaleConfig,
    SecretsConfig,
    StorageConfig,
    Configuration
):
    # set the environment to production only in Production configuration file
    ENVIRONMENT = EnvChoices.local
