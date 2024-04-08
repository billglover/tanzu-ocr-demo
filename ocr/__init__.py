import os
import logging
from logging.config import dictConfig

from flask import Flask
from ocr import pages, images

def create_app():
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    "formatter": "default",
                }
            },
            "root": {"level": "DEBUG", "handlers": ["console"]},
        }
    )

    app = Flask(__name__)
    app.secret_key = b'sadfsdfhrtewthbdag'
    app.config.from_prefixed_env("APP")
    
    # ensure the images folder exists
    try:
        os.makedirs(os.path.join(app.instance_path, app.config["IMAGES_DIR"]))
    except OSError:
        pass

    app.register_blueprint(pages.bp)
    app.register_blueprint(images.bp)

    app.logger.info("Current Environment: %s", app.config["ENVIRONMENT"])

    return app