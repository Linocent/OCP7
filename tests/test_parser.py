import pytest
from Grandpy.my_parser import MyParser
from Grandpy.api_request import WikiApi, GoogleApi


def test_parser():
    q2 = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer " \
         "l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."
    q1 = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y " \
         "pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
    expected_a = "musée art histoire fridbourg"
    expected_b = "tour eiffel"

    assert MyParser.my_parse(q1) == expected_a
    assert MyParser.my_parse(q2) == expected_b


class WikiApiTest:
    def __init__(self):
        pass

    def test_wiki(self, monkeypatch):

        class MockResponse:
            status_code = 200

            def json(self):
                return {'warnings':
                           {'main':
                                {'*': 'Unrecognized parameter: gradius.'}},
                       'batchcomplete': '',
                       'query':
                           {'geosearch':
                                [{'pageid': 504400,
                                  'ns': 0,
                                  'title': 'Porte de la Villette (Paris Métro)',
                                  'lat': 48.89709,
                                  'lon': 2.38588,
                                  'dist': 187.4,
                                  'primary': ''},
                                 {'pageid': 19291327,
                                  'ns': 0,
                                  'title': 'Canal Saint-Denis',
                                  'lat': 48.9,
                                  'lon': 2.3833333333333333,
                                  'dist': 276.3,
                                  'primary': ''},
                                 {'pageid': 504402,
                                  'ns': 0,
                                  'title': 'Corentin Cariou (Paris Métro)',
                                  'lat': 48.89434,
                                  'lon': 2.381745,
                                  'dist': 373.2,
                                  'primary': ''},
                                 {'pageid': 3419192,
                                  'ns': 0,
                                  'title': "Cité des Sciences et de l'Industrie",
                                  'lat': 48.895556,
                                  'lon': 2.388056,
                                  'dist': 404.2,
                                  'primary': ''},
                                 {'pageid': 11352411,
                                  'ns': 0,
                                  'title': "École nationale supérieure d'architecture de Paris-La Villette",
                                  'lat': 48.89361111111111,
                                  'lon': 2.381111111111111,
                                  'dist': 465.3,
                                  'primary': ''}]}}

        def mock_get(self, *args, **kwargs):
            return MockResponse()

        monkeypatch.setattr('rq.get', mock_get)
        wiki_test = WikiApi.wiki_request_title(48.8975156, 2.3833993)
        assert wiki_test == ["J'ai grandis juste à côté, laisse moi te parler de cet endroit.",
                             "L'École nationale supérieure d'architecture de Paris-La Villette (ENSAPLV) est un "
                             "établissement public d'enseignement supérieur à caractère administratif situé à Paris en "
                             "France. Elle est placée sous la tutelle du ministère de la Culture et de la Communication"
                             " (direction de l'Architecture et du Patrimoine). C'est l'une des vingt écoles publiques —"
                             " les écoles nationales supérieures d'architecture — qui dispensent un enseignement "
                             "supérieur de l'architecture en France.\nL'école de Paris-La Villette est, par le nombre "
                             "de ses étudiants, la plus importante des 22 écoles d'architecture habilitées en France. "
                             "Elle est membre de la Communauté d’universités et établissements (COMUE) HESAM.- HeSam "
                             "Université (hautes études Sorbonne arts et métiers) est une ComUE (Communauté "
                             "d'Universités et d'Établissements) qui fédère 12 établissements français d’enseignement "
                             "supérieur, de formation et de recherche.\nEx-UP6 (unité pédagogique no 6), l'école est "
                             "principalement située au 144 avenue de Flandre / 9 rue Barbanègre (avec également des "
                             "locaux 11 rue de Cambrai pour le libre service informatique, et 118-130 avenue "
                             "Jean-Jaurès pour les laboratoires de recherche), dans le 19e arrondissement de Paris.",
                             'https://fr.wikipedia.org/wiki/%C3%89cole_nationale_sup%C3%A9rieure_d%27architecture_de_'
                             'Paris-La_Villette']


class GoogleAPI:

    def __init__(self):
        pass

    def test_Google(self, monkeypatch):

        class MockResponse:
            status_code =200

            def json(self):
                return {'candidates':
                         [{'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                           'geometry': {'location': {'lat': 48.8975156, 'lng': 2.3833993},
                                        'viewport': {'northeast': {'lat': 48.89886702989273, 'lng': 2.384756379892722},
                                                     'southwest': {'lat': 48.89616737010729, 'lng': 2.382056720107278}}},
                           'name': 'OpenClassrooms'}],
                     'status': 'OK'}

        def mock_get(self, *args, **kwargs):
            return MockResponse()

        monkeypatch.setattr('rq.get', mock_get)
        google_test = GoogleApi.google_request('openclassrooms')
        assert google_test == {'address': '10 Quai de la Charente, 75019 Paris, France', 'name': 'OpenClassrooms',
                               'lati': 48.8975156, 'lngi': 2.3833993}




"""
Google_API_Result = {'candidates':
                         [{'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                           'geometry': {'location': {'lat': 48.8975156, 'lng': 2.3833993},
                                        'viewport': {'northeast': {'lat': 48.89886702989273, 'lng': 2.384756379892722},
                                                     'southwest': {'lat': 48.89616737010729, 'lng': 2.382056720107278}}},
                           'name': 'OpenClassrooms'}],
                     'status': 'OK'}

Wiki_API_result = {'warnings':
                           {'main':
                                {'*': 'Unrecognized parameter: gradius.'}},
                       'batchcomplete': '',
                       'query':
                           {'geosearch':
                                [{'pageid': 504400,
                                  'ns': 0,
                                  'title': 'Porte de la Villette (Paris Métro)',
                                  'lat': 48.89709,
                                  'lon': 2.38588,
                                  'dist': 187.4,
                                  'primary': ''},
                                 {'pageid': 19291327,
                                  'ns': 0,
                                  'title': 'Canal Saint-Denis',
                                  'lat': 48.9,
                                  'lon': 2.3833333333333333,
                                  'dist': 276.3,
                                  'primary': ''},
                                 {'pageid': 504402,
                                  'ns': 0,
                                  'title': 'Corentin Cariou (Paris Métro)',
                                  'lat': 48.89434,
                                  'lon': 2.381745,
                                  'dist': 373.2,
                                  'primary': ''},
                                 {'pageid': 3419192,
                                  'ns': 0,
                                  'title': "Cité des Sciences et de l'Industrie",
                                  'lat': 48.895556,
                                  'lon': 2.388056,
                                  'dist': 404.2,
                                  'primary': ''},
                                 {'pageid': 11352411,
                                  'ns': 0,
                                  'title': "École nationale supérieure d'architecture de Paris-La Villette",
                                  'lat': 48.89361111111111,
                                  'lon': 2.381111111111111,
                                  'dist': 465.3,
                                  'primary': ''}]}}


class MockRequestsGet:
    def __init__(self, url, params=None):
        pass

    def json(self):
        return FAKE_API_RESULT



"""
"""
This is url: https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=openclassrooms&inputtype=textquery&fields=formatted_address%2Cname%2Cgeometry&language=fr&key=AIzaSyCBGitJm3ohngupPAnm-m0kFowgqxzT0eU
This is response.json: {'candidates': [{'formatted_address': '10 Quai de la Charente, 75019 Paris, France', 'geometry': {'location': {'lat': 48.8975156, 'lng': 2.3833993}, 'viewport': {'northeast': {'lat': 48.89886702989273, 'lng': 2.384756379892722}, 'southwest': {'lat': 48.89616737010729, 'lng': 2.382056720107278}}}, 'name': 'OpenClassrooms'}], 'status': 'OK'}
This is information: {'address': '10 Quai de la Charente, 75019 Paris, France', 'name': 'OpenClassrooms', 'lati': 48.8975156, 'lngi': 2.3833993}
gp answer: ["J'ai grandis juste à côté, laisse moi te parler de cet endroit.", "L'École nationale supérieure d'architecture de Paris-La Villette (ENSAPLV) est un établissement public d'enseignement supérieur à caractère administratif situé à Paris en France. Elle est placée sous la tutelle du ministère de la Culture et de la Communication (direction de l'Architecture et du Patrimoine). C'est l'une des vingt écoles publiques — les écoles nationales supérieures d'architecture — qui dispensent un enseignement supérieur de l'architecture en France.\nL'école de Paris-La Villette est, par le nombre de ses étudiants, la plus importante des 22 écoles d'architecture habilitées en France. Elle est membre de la Communauté d’universités et établissements (COMUE) HESAM.- HeSam Université (hautes études Sorbonne arts et métiers) est une ComUE (Communauté d'Universités et d'Établissements) qui fédère 12 établissements français d’enseignement supérieur, de formation et de recherche.\nEx-UP6 (unité pédagogique no 6), l'école est principalement située au 144 avenue de Flandre / 9 rue Barbanègre (avec également des locaux 11 rue de Cambrai pour le libre service informatique, et 118-130 avenue Jean-Jaurès pour les laboratoires de recherche), dans le 19e arrondissement de Paris.", 'https://fr.wikipedia.org/wiki/%C3%89cole_nationale_sup%C3%A9rieure_d%27architecture_de_Paris-La_Villette']
"""