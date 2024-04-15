FROM demo.goharbor.io/bglover-vac/easy-ocr-base:latest

RUN mkdir /.EasyOCR
RUN chown 1000:1000 /.EasyOCR

WORKDIR /app
COPY . /app

EXPOSE 8080
CMD ["/usr/local/bin/gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]