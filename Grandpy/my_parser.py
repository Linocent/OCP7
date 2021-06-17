#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Timothée 2021-06-17
This file is part of project [OCP7](https://github.com/Linocent/OCP7).
"""
import json
import re
import unidecode


class MyParser:
    """This class is about the parser."""

    def __init__(self):
        pass

    @staticmethod
    def my_parse(sentence: str):
        """This function take the question and delete all words which
        are contain in ban_words.json in order to have keywords."""

        with open('grandpy/ban_words.json') as ban_word:
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
