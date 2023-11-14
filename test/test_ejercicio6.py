from src.ejercicio6 import *
import pytest

def test_unir():
    assert unir({'a', 'e', 'i', 'o', 'u'},{'b','c','d','f','g','h','j','k','l','m','n','ñ','p','q','r','s','t','v','w','x','y','z'}) == {'b', 'c', 'g', 'l', 'e', 'd', 'q', 'f', 'n', 't', 'y', 'p', 'x', 'z', 'v', 'w', 'i', 'a', 'k', 's', 'o', 'h', 'm', 'r', 'u', 'j','ñ'}