import os
from glob import glob

workers = int(os.environ.get('GUNICORN_PROCESSES', '1'))
threads = int(os.environ.get('GUNICORN_THREADS', '4'))
# timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))
bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8080')

loglevel = 'info'
reload = True
reload_extra_files = glob('ocr/**/*.html', recursive=True) + glob('ocr/**/*.css', recursive=True)
errorlog = '-'
accesslog = '-'

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }