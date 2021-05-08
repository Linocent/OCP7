import json
import re
import unidecode


def parse(sentence: str):

    with open('ban_words.json') as ban_word:
        data_dict = json.load(ban_word)
    sentence = unidecode.unidecode(sentence)
    lowered = sentence.lower()
    removed_signs = re.sub("[!@#$?,:;.]", '', lowered)
    removed_union_straight = re.sub("[-]", " ", removed_signs)
    keyword = re.split(" |'", removed_union_straight)
    filtered = []
    for word in keyword:
        if word not in data_dict:
            filtered.append(word)
    print(f"this is filtered: {filtered}")
    return filtered


parse("Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y "
      "pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?")
