import pytest

from utils import str_to_bool

""" Forma larga de probar todas las posibles opciones 
def test_yes_is_true():
    result = str_to_bool('yes')
    assert result is True
    
def test_y_is_true():
    result = str_to_bool('y')
    assert result is True
 """    
 
#  Utilizando parametros
@pytest.mark.parametrize('value', ['y', 'yes', '', 'n'])
def test_is_true(value):
    result = str_to_bool(value)
    assert result is True