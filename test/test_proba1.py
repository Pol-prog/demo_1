import pytest


@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('\nAfter test')

def test_1():
    assert 1 == 1

def test_2(before_after):
    assert 2 == 2