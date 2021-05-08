import pytest
from . import parse


def test_parser():

    a = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y " \
        "pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
    b = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer " \
        "l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."
    expected_a = "musée art histoire fridbourg"
    expected_b = "tour eiffel"

    assert parse(a) == expected_a
    assert parse(b) == expected_b

