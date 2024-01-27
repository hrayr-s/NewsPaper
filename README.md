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
You can deploy current project on your own computer for development or testing purposes without any server configuration
 or using Nginx web server with uwsgi python module.

## Local server deployment for development
Download Anaconda environment manager from https://www.anaconda.com/ and install it on your computer.
Open Terminal(Ubuntu/Linux/Mac) / Command Line(Windows) in the project root folder and make sure anaconda(conda) is working properly.
Run following command to install requirements for project.
- ``conda env create -f=environment.yml``

After installation is done change environment using command below:
- ``conda activate NewsPaper``

Use following commands to install and run the project:
1. ``python manage.py migrate``
2. ``python manage.py runserver``

When server runs successfully it will output something like this:
```System check identified no issues (0 silenced).
December 11, 2020 - 17:38:55
Django version 3.1.4, using settings 'NewsPaper.settings.development'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Open browser and go with URL http://127.0.0.1:8000/

## Public Server deployment
You can find instructions for deployment on nginx server in the internet.
