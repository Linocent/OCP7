from flask import Flask, render_template, request, jsonify
from my_parser import MyParser
from api_request import GoogleApi


app = Flask(__name__)


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyse/', methods=['GET'])
def analyse():
    user_input = request.args["question"]
    keyword = MyParser.my_parse(user_input)
    GoogleApi.google_request(keyword)

    return jsonify(
        user_input=user_input
    )


if __name__ == "__main__":
    app.run()
