from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(64))
    highest_grade = db.Column(db.String(7))


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64)) # "Guide Route Left",
    area = db.Column(db.String(256)) # "1) Super Mario Boulder > Beauty Mountain > New River Gorge Proper > The New River Gorge Region > West Virginia",
    mp_link = db.Column(db.String(128)) # https://www.mountainproject.com/route/105944154/guide-route-left,2.0,-1,
    _type = db.Column(db.String(32)) # "Trad, TR",
    yds = db.Column(db.String(16)) # 5.10a/b+ PG13,
    pitches = db.Column(db.Integer) # 1
    length = db.Column(db.Integer) # 30
    lat = db.Column(db.Float) # 38.05531,
    long = db.Column(db.Float) # -81.0362