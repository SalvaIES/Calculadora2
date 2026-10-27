import sys
from pathlib import Path

# Obtiene la ruta del directorio padre (un nivel arriba)
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from calculadora import sumar, restar


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
    assert sumar(-5, -3) == -8
    assert sumar(2.5, 3.5) == 6.0


def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 0) == 0
    assert restar(-1, -1) == 0
    assert restar(10, 5) == 5
    assert restar(2.5, 1.5) == 1.0
