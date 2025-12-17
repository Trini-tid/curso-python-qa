from _pytest.fixtures import fixture
from test.config import Config

def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action='store',
        help='Ambiente de ejecucion de pruebas [dev, qa]'
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption('--env')


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg