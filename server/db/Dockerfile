# pull official base image
FROM postgres:13.4-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
