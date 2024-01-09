from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16))
    highest_grade = db.Column(db.String(7))

# 5.12a
# 1234567
# 5.11a/b