from flask import url_for

from main import app


def route(path):
    # print("1111" + str(app.url_map.__dict__))
    print(str(url_for(path)))

    if path in app.url_map.__dict__:
        print("in url_map")
        return path
    else:
        print("not in url_map")
        return find_route(path)


def find_route(path):
    strs = path.split('/')
    return path
