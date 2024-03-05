FROM python:3.11-slim-bookworm as base
LABEL authors="hrayr <i@hrayr.am>"
WORKDIR /opt/project

#RUN apt install python3-venv python3-pip python3-poetry
RUN python -m pip install poetry

COPY . .

RUN python -m poetry install --sync
#ENTRYPOINT ["python", "manage.py runserver"]

FROM base as local
# app repo host directory should be mounted here on run
RUN echo "-> local"
RUN python -m poetry install --sync --with dev
