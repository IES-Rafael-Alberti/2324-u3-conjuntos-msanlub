from src.ejercicio4 import *
import pytest

def test_frutasIguales():
    assert frutasIguales({"manzana","pera"},{"manzana","naranja"}) == {"manzana"}

def test_frutasDesigualesEnUno():
    assert frutasDesigualesEnUno({"manzana", "pera", "naranja", "plátano", "uva"},{"manzana", "pera", "durazno", "sandía", "uva"}) == {'naranja', 'plátano'}

def test_frutasDesigualesenDos():
    assert frutasDesigualesEnDos({"manzana", "pera", "naranja", "plátano", "uva"},{"manzana", "pera", "durazno", "sandía", "uva"}) == {'sandía', 'durazno'}