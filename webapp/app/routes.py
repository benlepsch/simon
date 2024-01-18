from flask import render_template, redirect, url_for, flash, request, session
from app import app, db
from app.models import User

import hashlib

def loggedin():
    try:
        db.session.execute(db.select(User).filter_by(username=session['username'])).scalar_one()
    except:
        return False
    return True

@app.route('/updatedb')
def updatedb():
    # upd = ''
    # for user in db.session.execute(db.select(User)).scalars():
    #     if user.password == None:
    #         user.password = hashlib.sha256('password'.encode()).hexdigest()
    # db.session.commit()

    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # check for duplicate username
        uname = request.form['username']
        hg = request.form['highestgrade']
        pword = hashlib.sha256(request.form['password'].encode()).hexdigest()
        new = User(username=uname, highest_grade=hg, password=pword)
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pword = hashlib.sha256(request.form['password'].encode()).hexdigest()
        if uname == '':
            # print('error: blank')
            flash('Username cannot be blank')
            return redirect(url_for('login'))
        try:
            db.session.execute(db.select(User).filter_by(username=uname, password=pword)).scalar_one()
            # print(check)
        except:
            # print('excepting')
            flash('Username or password was incorrect')
            return redirect(url_for('login'))

        session['username'] = uname
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/editprofile', methods=['GET','POST'])
def editprofile():
    if not loggedin():
        return redirect(url_for('login'))
    if request.method == 'POST':
        updating = db.session.execute(db.select(User).filter_by(username=session['username'])).scalar_one()
        updating.highest_grade = request.form['highestgrade']

        db.session.commit()
        return redirect(url_for('editprofile'))
    hiG = db.session.execute(db.select(User).filter_by(username=session['username'])).scalar_one().highest_grade
    return render_template('editprofile.html', hg=hiG)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/delaccount')
def delaccount():
    if not loggedin():
        return redirect(url_for('login'))
    try:
        user = db.session.execute(db.select(User).filter_by(username=session['username'])).scalar_one()
        db.session.delete(user)
        db.session.commit()
        session.pop('username')
    except:
        flash('something broke sorby')
        return redirect(url_for('index'))
    flash('account deleted successfully')
    return redirect(url_for('index'))