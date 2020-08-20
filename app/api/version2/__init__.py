from flask import Blueprint

test2 = Blueprint('version2', __name__, url_prefix="/v2/")

from . import test

print("333")
