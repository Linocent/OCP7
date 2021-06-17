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
    #keyword = MyParser.my_parse(user_input)
    #information = GoogleApi.google_request(keyword)
    #title = WikiApi.wiki_request_title(information['lati'], information['lngi'])
    #texte = WikiApi.extract_text(title['title'])
    #gp_history = WikiApi.message(texte['summary'], texte['url'])
    #print(f"message: {message}")
    return jsonify(
        user_input=user_input,
        #gp_history=gp_history,
        #information=information,
        information="10 Quai de la Charente, 75019 Paris, France",
        gp_history=["J'ai grandis juste à côté, laisse moi te parler de cet endroit.",
                    "L'École nationale supérieure d'architecture de Paris-La Villette (ENSAPLV) est un établissement "
                    "public d'enseignement supérieur à caractère administratif situé à Paris en France. "
                    "Elle est placée sous la tutelle du ministère de la Culture et de la Communication (direction de "
                    "l'Architecture et du Patrimoine). C'est l'une des vingt écoles publiques — les écoles nationales "
                    "supérieures d'architecture — qui dispensent un enseignement supérieur de l'architecture en France.\n"
                    "L'école de Paris-La Villette est, par le nombre de ses étudiants, la plus importante des 22 écoles "
                    "d'architecture habilitées en France. Elle est membre de la Communauté d’universités et "
                    "établissements (COMUE) HESAM.- HeSam Université (hautes études Sorbonne arts et métiers) est une "
                    "ComUE (Communauté d'Universités et d'Établissements) qui fédère 12 établissements français "
                    "d’enseignement supérieur, de formation et de recherche.\nEx-UP6 (unité pédagogique no 6), "
                    "l'école est principalement située au 144 avenue de Flandre / 9 rue Barbanègre (avec également des "
                    "locaux 11 rue de Cambrai pour le libre service informatique, et 118-130 avenue Jean-Jaurès pour "
                    "les laboratoires de recherche), dans le 19e arrondissement de Paris.",
                    'https://fr.wikipedia.org/wiki/%C3%89cole_nationale_sup%C3%A9rieure_d%27architecture_de_Paris-La_Villette']
    )


if __name__ == "__main__":
    app.run()
