FROM demo.goharbor.io/bglover-vac/easy-ocr-base:latest

USER 0:0

WORKDIR /app
COPY . /app

EXPOSE 8080
CMD ["/usr/local/bin/gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]