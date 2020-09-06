import os
from functools import wraps
from flask import render_template, send_file, abort
from app import UPL, app




def normalize_path(path, follow_symlinks=True):
    if follow_symlinks:
        return os.path.realpath(path)
    return os.path.abspath(path)

def is_safe_path(basedir, path):
    return path.startswith(basedir)

def check_and_transform_path(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        path = normalize_path(kwargs.get("path", UPL))

        if not is_safe_path(UPL, path) or not os.path.exists(path):
            abort(404)

        kwargs["path"] = path

        return f(*args, **kwargs)

    return wrapper



@app.route('/upl')
@app.route('/upl/<path:path>')
@check_and_transform_path
def upl(path=None):
    entries = os.scandir(path)

    prev_dir = None
    if path and path != UPL:
        prev_dir = os.path.relpath(os.path.dirname(path), UPL)

    return render_template("upl.html", entries=entries,prev_dir=prev_dir)

@app.route("/download/<path:path>")
@check_and_transform_path
def download(path):
    return send_file(path)

