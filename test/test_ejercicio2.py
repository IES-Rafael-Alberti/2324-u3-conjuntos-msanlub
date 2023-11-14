from src.ejercicio2 import *
import pytest

def test_nombreTodosLosAlumnos():
    assert nombreTodosLosAlumnos({"marta"},{"julia"}) == {"marta","julia"}

def test_nombreRepetidor():
    assert nombreRepetidos({"maria"},{"maria"}) == {"maria"}

def test_nombreNoRepetidos():
    assert nombreNoRepetidos({"natalia"},{"marta"}) == {"natalia"}

def test_nombreIncluidos():
    assert nombreIncluidos({"maria"},{"maria"}) == True