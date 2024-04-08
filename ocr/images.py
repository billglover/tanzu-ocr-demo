import logging
from flask import Blueprint, render_template, redirect, request, url_for, flash,  current_app
from werkzeug.utils import secure_filename
import easyocr
import os

reader = easyocr.Reader(['ch_sim','en'], gpu=False, model_storage_directory="models", download_enabled=False)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

bp = Blueprint("images", __name__)

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route("/create", methods=("GET", "POST"))
def create():
  if request.method == "POST":
    author = request.form["author"] or "Anonymous"
    

    if request.files:
      file = request.files["image"]

      current_app.logger.info("Filename: %s", file.
                              filename)
      # do things here
      if file.filename == '':
        flash('No selected file')
        return render_template("images/create.html")
      if file and allowed_file(file.filename):
        filename = os.path.join(current_app.instance_path, current_app.config["IMAGES_DIR"], secure_filename(file.filename))
        file.save(filename)
        parsed = reader.readtext(filename)
        lines = map(lambda x: {"text": x[1], "bounds": x[0], "confidence": x[2]}, parsed)

        result={
           "author": author,
           "lines": lines,
           "image": secure_filename(file.filename)
        }
        return render_template("images/result.html", result=result)

  return render_template("images/create.html")

@bp.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(os.path.join(current_app.instance_path, current_app.config["IMAGES_DIR"]), filename)
