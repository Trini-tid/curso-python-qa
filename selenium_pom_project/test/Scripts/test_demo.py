def test_environment_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myapp.qa.com'
    assert port == '80'


def test_environment_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myapp.qa.com'
    assert port == '80'





