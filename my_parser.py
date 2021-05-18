import json
import re
import unidecode


class MyParser:

    def __init__(self):
        pass

    @staticmethod
    def my_parse(sentence: str):

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



