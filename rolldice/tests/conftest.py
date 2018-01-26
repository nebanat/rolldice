import pytest

from rolldice.app import create_app


@pytest.yield_fixture(scope='session')
def app():
    """
    setup our flask test app, this only gets executed once.

    :return: Flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True
    }

    _app = create_app(settings_override=params)

    # Establish an application context before running test
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """
    setup an app client, this gets executed for each test function

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()
