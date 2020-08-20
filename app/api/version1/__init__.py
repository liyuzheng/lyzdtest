from flask import Blueprint

test1 = Blueprint('version1', __name__, url_prefix="/v1/")

from . import test, interceptor

print("333")
