FROM demo.goharbor.io/bglover-vac/easy-ocr-base:latest
WORKDIR /app
COPY . /app

EXPOSE 8080
CMD ["/usr/local/bin/gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]