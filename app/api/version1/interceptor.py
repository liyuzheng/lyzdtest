from werkzeug.utils import redirect

from app.api.version1 import test1
from flask import request, url_for

from main import app



@test1.before_request
def before_request():
    print("111333222")
    s = request.path
    print(s)
    # return redirect(url_for("version1.testUu"))


@test1.after_request
def after_request(environ):
    print("after_request")
    return environ
