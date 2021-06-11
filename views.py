from flask import Flask, render_template, request, jsonify
from my_parser import MyParser
from api_request import GoogleApi, WikiApi


app = Flask(__name__)


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyse/', methods=['GET'])
def analyse():
    user_input = request.args["question"]
    keyword = MyParser.my_parse(user_input)
    #information = GoogleApi.google_request(keyword)
    #message = WikiApi.wiki_request_title(information['lati'], information['lngi'])
    #print(f"message: {message}")
    return jsonify(
        user_input=user_input,
        #gp_history=message,
        #information=information,
        information="10 Quai de la Charente, 75019 Paris, France"
    )


if __name__ == "__main__":
    app.run()
