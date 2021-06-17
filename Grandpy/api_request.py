from config import GOOGLE_API_KEY
import requests as rq
import wikipedia as wp
import random as rd


class GoogleApi:
    """This class use Google maps API to work. Link of the documentation of API:
    https://developers.google.com/maps/documentation/places/web-service/search?hl=fr"""

    def __init__(self):

        self.key = GOOGLE_API_KEY

    def google_request(self, user_input: str):
        """ This fonction search information about the place, like adresse, name and coordonates."""

        information = dict()
        URL = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
        KEY = self.key
        params = {"input": user_input,
                  "inputtype": "textquery",
                  "fields": "formatted_address,name,geometry",
                  "language": "fr",
                  "key": KEY}
        request = rq.get(URL, params=params)
        #print(f"This is url: {request.url}")
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
        # else:
            # print(f"Error, code: {request.status_code}")


class WikiApi:
    """This class use mediawiki API in order to find information about place find. Documentation of API:
    https://www.mediawiki.org/wiki/MediaWiki"""

    def __init__(self):

        self.INTRO = ["Tiens, ce que tu me demande me rappel une histoire. Assieds-toi et écoute:",
                      "Mais bien sûr, je me souviens.",
                      "J'ai grandis juste à côté, laisse moi te parler de cet endroit."]
        self.URL = "https://en.wikipedia.org/w/api.php"

    def wiki_request_title(self, lat: float, lng: float):
        """Fin a random place with coords of the place."""

        page_title = dict()
        params = {
            "action": "query",
            "format": "json",
            "list": "geosearch",
            "gscoord": f"{lat}|{lng}",
            "gslimit": '10',
            "gradius": '1000'
        }
        request = rq.get(self.URL, params=params)
        #print(f"This is url: {request.url}")
        response = request.json()
        print(f"wiki_response: {response}")
        result = response['query']['geosearch']
        for place in result:
            page_title['title'] = place['title']
        print(f"page_title: {page_title}")
        return page_title

    def extract_text(self, title: str):
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
        random_intro = self.INTRO[rd.randint(0, len(self.INTRO)-1)]
        grandpy_answer.append(random_intro)
        grandpy_answer.append(summary)
        grandpy_answer.append(url)
        print(f"gp answer: {grandpy_answer}")
        return grandpy_answer


GoogleApi = GoogleApi()  # J'instancie ma classe
WikiApi = WikiApi()
# WikiApi.wiki_request_title(48.8975156, 2.3833993)
WikiApi.extract_text("École nationale supérieure d'architecture de Paris-La Villette")
# GoogleApi.google_request("OpenClassroom")
