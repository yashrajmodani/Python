from flask import Flask, render_template, request, redirect, url_for


survey = Flask(__name__)

@survey.route('/')
def homePage():
    return render_template('homePage.html')

@survey.route('/survey')
def surveyForm():
    return render_template('survey.html')
#
@survey.route('/display', methods=['Post'])
def display():
    print("Survey Result")
    name = request.form['name']
    email = request.form['email']
    satis = request.form['satisfaction']
    others = request.form['recommend']
    return f"Name: {name}\n, \nemail: {email}, \nsatisfaction Level: {satis}, \nRecommend to others: {others} "


if __name__ == '__main__':
    survey.run(port=5001, debug=True)
