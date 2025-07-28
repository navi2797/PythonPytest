import pytest

@pytest.fixture(autouse=True,scope='session')
def global_setup():
    print("starting the setup")
    yield
    print("closing the setup")