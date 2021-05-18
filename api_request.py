from config import GOOGLE_API_KEY
import requests as rq


class GoogleApi:
    """This class use Google maps API to work. Link of the documentation of API:
    https://developers.google.com/maps/documentation/places/web-service/search?hl=fr"""

    def __init__(self):

        pass

    def google_request(self, user_input: str):
        """ This fonction search information about the place, like adresse, name and coordonates."""

        information = dict()
        URL = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
        KEY = GOOGLE_API_KEY
        params = {"input": user_input, "inputtype": "textquery", "fields": "formatted_address,name,geometry",
                       "language": "fr", "key": KEY}
        request = rq.get(URL, params=params)
        print(f"This is url: {request.url}")
        if request.status_code == rq.codes.ok:
            response = request.json()
            result = response['candidates'][0]
            information['address'] = result['formatted_address']
            information['name'] = result['name']
            information['lat'] = result['geometry']['location']['lat']
            information['lng'] = result['geometry']['location']['lng']
            print(f"This is information: {information}")
            WikiApi.wiki_request_title(information['lat'], information['lng'])
            return information
        else:
            print(f"Error, code: {request.status_code}")


class WikiApi:
    """This class use mediawiki API in order to find information about place find. Documentation of API:
    https://developers.google.com/maps/documentation/places/web-service/search?hl=fr"""

    def __init__(self):

        self.INTRO = ["Tiens, ce que tu me demande me rappel une histoire. Assieds-toi et écoute",
                      "Mais bien sûr, je me souviens.",
                      "J'ai grandis juste à côté, laisse moi te parler de cet endroit."]
        self.title_id = dict()
        self.URL = "https://en.wikipedia.org/w/api.php"

    def wiki_request_title(self, lat: float, lng: float):
        """Fin a random place with coords of the place."""

        params = {
            "action": "query",
            "format": "json",
            "list": "geosearch",
            "gscoord": f"{lat}|{lng}",
            "gslimit": '10',
            "gradius": '1000'
        }
        request = rq.get(self.URL, params=params)
        print(f"This is url: {request.url}")
        response = request.json()
        result = response['query']['geosearch']
        for place in result:
            self.title_id['title'] = place['title']
            self.title_id['text_id'] = place['pageid']
        print(f"This is title: {self.title_id}")
        WikiApi.extract_text(self.title_id['title'], self.title_id['text_id'])

    def extract_text(self, title: str, text_id: int):
        """This function find description of the random place found."""

        story_place = dict()
        """params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": title
        }"""
        params = {
            "action": "parse",
            "page": title,
            "format": "json"
        }
        request = rq.get(self.URL, params=params)
        response = request.json()
        print(f"This is URL: {request.url}")
        result = response['query']['search']
        print(f"This is result: {result}")


GoogleApi = GoogleApi()  # J'instancie ma classe
WikiApi = WikiApi()
WikiApi.wiki_request_title(48.856614, 2.3522219)
# GoogleApi.google_request("OpenClassroom")

# This is information: {'address': 'Paris, France', 'name': 'Paris', 'lat': 48.856614, 'lng': 2.3522219}
# This is information: {'address': '10 Quai de la Charente, 75019 Paris, France', 'name': 'OpenClassrooms',\
    # 'lat': 48.8975156, 'lng': 2.3833993}


