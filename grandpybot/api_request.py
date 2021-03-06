#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Timothée 2021-06-17
This file is part of project [OCP7](https://github.com/Linocent/OCP7).
"""
import random as rd
import requests as rq
import wikipedia as wp
from config import GOOGLE_API_KEY


class GoogleApi:
    """This class use Google maps API to work. Link of the documentation of API:
    https://developers.google.com/maps/documentation/places/web-service/search?hl=fr"""

    def __init__(self):

        self.key = GOOGLE_API_KEY

    def google_request(self, user_input: str):
        """ This fonction search information about the place,
        like adresse, name and coordonates."""

        information = dict()
        url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
        key = self.key
        params = {"input": user_input,
                  "inputtype": "textquery",
                  "fields": "formatted_address,name,geometry",
                  "language": "fr",
                  "key": key}
        request = rq.get(url, params=params)
        print(f"This is url: {request.url}")
        if request.status_code == rq.codes.ok:
            response = request.json()
            print(f"This is response.json: {response}")
            result = response['candidates'][0]
            information['address'] = result['formatted_address']
            information['name'] = result['name']
            information['lati'] = result['geometry']['location']['lat']
            information['lngi'] = result['geometry']['location']['lng']
            print(f"This is information: {information}")
            return information


class WikiApi:
    """This class use mediawiki API in order to find information
    about place find. Documentation of API:
    https://www.mediawiki.org/wiki/MediaWiki"""

    def __init__(self):

        self.intro = ["Tiens, ce que tu me demande me rappel une histoire. "
                      "Assieds-toi et écoute:",
                      "Mais bien sûr, je me souviens.",
                      "J'ai grandis juste à côté, laisse moi te "
                      "parler de cet endroit."]
        self.url = "https://en.wikipedia.org/w/api.php"

    def wiki_request_title(self, lat: float, lng: float):
        """Find a random place with coords of the place."""

        page_title = dict()
        params = {
            "action": "query",
            "format": "json",
            "list": "geosearch",
            "gscoord": f"{lat}|{lng}",
            "gslimit": '10',
            "gradius": '1000'
        }
        request = rq.get(self.url, params=params)
        print(f"This is url: {request.url}")
        response = request.json()
        print(f"wiki_response: {response}")
        result = response['query']['geosearch']
        for place in result:
            page_title['title'] = place['title']
        print(f"page_title: {page_title}")
        return page_title

    @staticmethod
    def extract_text(title: str):
        """This function find description of the random place found."""

        info = dict()
        wp.set_lang("fr")
        page_title = wp.page(title)
        info['summary'] = page_title.summary
        info['url'] = page_title.url
        return info

    def message(self, summary, url):
        """This function take every element we need for the answer."""

        grandpy_answer = []
        random_intro = self.intro[rd.randint(0, len(self.intro)-1)]
        grandpy_answer.append(random_intro)
        grandpy_answer.append(summary)
        grandpy_answer.append(url)
        print(f"gp answer: {grandpy_answer}")
        return grandpy_answer


GoogleApi = GoogleApi()
WikiApi = WikiApi()
