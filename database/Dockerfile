FROM postgres:14

COPY init.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_DB=myapp
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

