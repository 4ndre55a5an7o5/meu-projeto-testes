import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import soma, subtracao, multiplicacao, divisao
import pytest

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(10, 5) == 5

def test_multiplicacao():
    assert multiplicacao(4, 2) == 8

def test_divisao():
    assert divisao(10, 2) == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)