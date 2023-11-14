from src.ejercicio5 import *
import pytest

def test_pares():
    assert pares({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) == {2, 4, 6, 8, 10}

def test_multiploTres():
    assert multiploTres({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) == {9, 3, 6}

def test_interseccion():
    assert interseccion({2, 4, 6, 8, 10},{9, 3, 6}) == {6}