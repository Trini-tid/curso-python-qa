from pytest import mark # pyright: ignore[reportMissingImports]

@mark.api
@mark.data
def test_prueba01():
    assert True
    
@mark.data
def test_prueba02():
    assert True
    
@mark.parametrize('nombre', ['juan', 'pedro', 'maria'])    
def test_prueba03(nombre):
    assert True 

@mark.ui
@mark.parametrize('nombre', ['juan', 'Pedro', 'maria'])    
def test_prueba04(nombre):
    print ("valor parametro: " + nombre)
    assert nombre in ['juan', 'pedro', 'maria', 'alex']