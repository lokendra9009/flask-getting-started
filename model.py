import json


def db_load():
    with open("blog.json") as f:
        return json.load(f)


def save_db():
    with open("blog.json", 'w') as f:
        return json.dump(db, f)


db = db_load()
