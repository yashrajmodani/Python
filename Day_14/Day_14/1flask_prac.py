from flask import Flask

app = Flask(__name__)

@app.route('/')
def homePage():
    return "Welcome to home Page!!"

if __name__ == '__main__':
    app.run(port=5001, debug=True)

