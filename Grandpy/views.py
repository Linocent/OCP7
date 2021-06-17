from flask import Flask, render_template, request, jsonify
from grandpy.my_parser import MyParser
from grandpy.api_request import GoogleApi, WikiApi


app = Flask(__name__)


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyse/', methods=['GET'])
def analyse():
    user_input = request.args["question"]
    keyword = MyParser.my_parse(user_input)
    information = GoogleApi.google_request(keyword)
    title = WikiApi.wiki_request_title(information['lati'], information['lngi'])
    texte = WikiApi.extract_text(title['title'])
    gp_history = WikiApi.message(texte['summary'], texte['url'])
    return jsonify(
        user_input=user_input,
        gp_history=gp_history,
        information=information,
           )


if __name__ == "__main__":
    app.run()
