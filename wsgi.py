import os
from ocr import create_app

os.environ['APP_IMAGES_DIR'] = "images"
os.environ['APP_ENVIRONMENT'] = 'dev'

app = create_app()
app.config["TEMPLATES_AUTO_RELOAD"] = True

if __name__ == '__main__':
    app.run()