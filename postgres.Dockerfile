FROM postgres:14-bullseye
# install postgres extensions
RUN apt-get update -y && apt-get install -y postgresql-14-repack postgresql-plpython3-14
USER postgres
