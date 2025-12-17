from pytest import mark

@mark.smoke
@mark.body
class TestBody:
    @mark.ui
    def test_body_functions(self):
        assert True
        
    def test_bumper(self):
        assert True
        
    def test_windshield(self):
        assert True