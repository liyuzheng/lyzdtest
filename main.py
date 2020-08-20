from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

from app.api.version1 import test1
from app.api.version2 import test2

app = Flask(__name__)
app.register_blueprint(test1)
app.register_blueprint(test2)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lyz:Lyz190019@81.70.19.176:3306/customsconsulation?charset=utf8'
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    # print(app.url_map)
    app.run()
