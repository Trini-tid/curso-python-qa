from pytest import mark

@mark.smoke
@mark.engine
def test_engine_function_pass():
    assert True