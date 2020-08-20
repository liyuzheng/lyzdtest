from app.api.version1 import test1
from app.models.user import insert
from main import db

print("222")


@test1.route('/test/uu/<userid>')
def testUu(userid):
    print("call testuu1")
    insert()
    return 'testuu1'


@test1.route("/create/db")
def create_db():
    print('begin drop')
    db.drop_all()
    print('end drop')
    db.create_all()
    return "111"
