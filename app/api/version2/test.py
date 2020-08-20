from app.api.version2 import test2

print("222")


@test2.route('/test/uu/')
def testUu():
    print("call testuu2")
    return 'testuu2'
