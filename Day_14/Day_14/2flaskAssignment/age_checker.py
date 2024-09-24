from flask import Flask, render_template, request, redirect, url_for

appLogin = Flask(__name__)

@appLogin.route('/')
def homePage():
    return render_template('homePage.html')

@appLogin.route('/ageChecker')
def ageForm():
    return render_template('ageChecker.html')

@appLogin.route('/displayAge', methods=['POST'])
def displayAge():
    age = request.form['age']
    name = request.form['name']

    if int(age) < 18:
        return f"{name}'s age is {age}. He is a minor."
    else:
        return redirect(url_for('result'))


@appLogin.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    appLogin.run(port=5001, debug=True)
