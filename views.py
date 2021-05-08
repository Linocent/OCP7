from flask import Flask, render_template, request

import parser

app = Flask(__name__)


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyse/', methods=['GET'])
def analyse():
    user_input = request.form
    print(f"user_input: {user_input}")
    parser.parse(user_input)


if __name__ == "__main__":
    app.run()
