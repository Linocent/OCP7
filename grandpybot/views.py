#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Timothée 2021-06-17
This file is part of project [OCP7](https://github.com/Linocent/OCP7).
"""
from flask import Flask, render_template, request, jsonify
from grandpybot.my_parser import MyParser
from grandpybot.api_request import GoogleApi, WikiApi

app = Flask(__name__)


@app.route('/index/')
@app.route('/')
def index():
    """This is the home page."""
    return render_template('index.html')


@app.route('/analyse/', methods=['GET'])
def analyse():
    """This where the user input will be analyse and the answer will send to front-end"""
    user_input = request.args["question"]
    keyword = MyParser.my_parse(user_input)
    information = GoogleApi.google_request(keyword)
    title = WikiApi.wiki_request_title(information['lati'],
                                       information['lngi'])
    texte = WikiApi.extract_text(title['title'])
    gp_history = WikiApi.message(texte['summary'], texte['url'])
    return jsonify(
        user_input=user_input,
        gp_history=gp_history,
        information=information,
           )


if __name__ == "__main__":
    app.run()
