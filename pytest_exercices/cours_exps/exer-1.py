
def str_to_int(string):
    error_msg="Unable to conver to integer: '%s'" % str(string)
    try:
        integer = float(string.replace(',', '.'))
    except AttributeError:
        if isinstance(string, (int, float)):
            integer = string
        else:
            raise RuntimeError(error_msg)
    except (TypeError, ValueError):
            raise RuntimeError(error_msg)
    
class TestStrToInt:
    
    def setup(self):
        print('\nthis is setup')
    
    def teardown(self):
        print('\nthis is teardown')
        
    def setup_class(cls):
        print('\nthis is setup class')
        
    def teardown_class(cls):
        print('\nthis is teardown')
    
    def test_round_down(self):
        result = str_to_int('1.99')
        assert result == 2   
        
    def test_round_down_lesser_half(self):
        result = str_to_int('1.2')
        assert result == 1
        
    def test_rainy_scenario(self):
        result = str_to_int('14, 35')
        assert result == 'Unable to conver to integer'
        
    