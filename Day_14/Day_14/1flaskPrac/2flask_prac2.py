from flask import Flask, render_template, request, redirect, url_for, session
from sympy.testing.runtests import method

#Step1: Initialize the flask app
appLogin = Flask(__name__)


##used for session data
appLogin.secret_key = 'secret'
print(appLogin)

#Step2: create a route for the login page
@appLogin.route('/')
def login():
    return render_template('login.html')

#Step3: Create a route to handle login form submission
@appLogin.route('/login', methods= ['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']

    #Srep4: simple username and password authentication
    if username == 'admin' and password == 'password':
        session['name'] = username
        # return f'Welcome, {username}'
        return redirect(url_for('show_dashboard'))
    else:
        return 'Invalid Credentials. Please Try Again!!!!!'
@appLogin.route('/dashboard')
def show_dashboard():
    name  = session.get('name')
    return render_template('dashboard.html', name=name)

#Step5: render flask app
if __name__ == '__main__':
    appLogin.run(port=5001, debug=True)

