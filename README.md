# NewsPaper
Python/Django Web Application for news site

A simple news portal using Django framework.

Control panel (Used Django Admin UI):

Administrator is able to create and modify news from admin panel using rich text editor (images not allowed in text editor).
Administrator is able to create categories and assign them to the news.
Any of news can have one or more categories but only one of them should be defined as "Main category".
News without main category are not allowed. 
    Example of categories: "Politics" "Business" "Tech" "Science" "Health", ets.
Available list views for categories and news
Available category and date filters for news list

Frontend part (Bootstrap 4 Example blog page):

Site has of next pages with their functionalities:

## Home page:
 - list of categories
 - list of all news from all categories

## Category page:
 - list of categories.
 - selected category should be highlighted
 - list of all news filtered selected category


## News detail page:
 - title of news
 - all related categories (are shown besides main category)
 - news content

Each item news in the listing represents title, main category and creation date.
News in the listing are paginated by 10 items.
News in the listing are ordered by creation date with descending direction.

# Deployment

The project can be deployed on a local computer for development or testing purposes without any server configuration
or using Nginx web server with uwsgi python module on a dedicated or virtual server.

In any case a `.env` file with required variables set is required. The file must be located in the project root. An
example of `.env` content is presented below.

```dotenv
SECRET_KEY="Some-Secret-Key"
DATABASE_URL=sqlite:///sqlite3.db
CACHE_URL=rediscache://127.0.0.1:6379/1?backend=django_redis.cache.RedisCache&client_class=django_redis.client.DefaultClient
ALLOWED_HOSTS=*
```

## Local server using Docker and docker-compose

To simply run the local server without any issues:

1. Install Docker Desktop: https://www.docker.com/products/docker-desktop/
2. Open Terminal/Command Line and run the following

```shell
docker-compose up -d
```

The installation and deployment will take time on first run, as it will download several packages required to run the
Python and deploy the project.

## Local server deployment for development

There are various ways to create local environment. Below are links to the common known:

- Anaconda (conda): Download Anaconda environment manager from https://www.anaconda.com/. A heavy python package manager
  with various tools to use.
- pyenv: The installation instructions are here https://github.com/pyenv/pyenv?tab=readme-ov-file#installation. This as
  well can be used to create local python environment with specific python version
- virtualenv (or venv): This can be used alongside with one of the soft
  above https://docs.python.org/3/library/venv.html. Separates project required packages/libraries from global python
  environment.

Open Terminal(Ubuntu/Linux/Mac) / Command Line(Windows) in the project root folder. Make sure virtual environment has
been created and activated using one of the options above before begin.

The project requires poetry installed. This is the package manager used for the prject. For that run:

```shell
python -m pip install poetry
```

To install project dependencies run following shell command.

```shell
poetry install --sync
```

Use following commands to install and run the project:
1. ``python manage.py migrate``
2. ``python manage.py runserver``

When server runs successfully it will output something like this:
```System check identified no issues (0 silenced).
December 11, 2020 - 17:38:55
Django version 3.1.4, using settings 'NewsPaper.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Open browser and go with URL http://127.0.0.1:8000/

## Public Server deployment

The instructions for deployment along with nginx server can be found in the internet.

# Locale

## Language configuration

You can configure languages using environment variables or .env variables.
To set default langauge use variable `DEFAULT_LANGUAGE_CODE`.
Note! The value from `DEFAULT_LANGUAGE_CODE` variable must be present in Languages list as language code.

Langauge configuration is a pair of language code and the name on that language (or whatever you want it to be
displayed).

Example of such configuration is present below:

```dotenv
LANGUAGES_LIST="ru|Русский,hy|Հայերեն,en|English"
DEFAULT_LANGUAGE_CODE=ru
```
