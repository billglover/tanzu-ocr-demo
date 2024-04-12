FROM python:3.11-bullseye as base

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

FROM python:3.11-bullseye as runtime
COPY --from=base /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=base /usr/local/bin/gunicorn /usr/local/bin/gunicorn

WORKDIR /app
COPY . /app

EXPOSE 8080
CMD ["/usr/local/bin/gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]