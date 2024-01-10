from flask import render_template, redirect, url_for, flash, request, session
from app import app, db
from app.models import User

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # check for duplicate username
        new = User(username=request.form['username'], highest_grade=request.form['highestgrade'])
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == '':
            # print('error: blank')
            flash('Username cannot be blank')
            return redirect(url_for('login'))
        try:
            check = db.session.execute(db.select(User).filter_by(username=request.form['username'])).scalar_one()
            # print(check)
        except:
            # print('excepting')
            flash('User with that name does not exist')
            return redirect(url_for('login'))

        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))