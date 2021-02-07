import pytest

import tests.factories as f


@pytest.fixture
def app(django_app):
    return django_app


@pytest.fixture
def staff_user(db):
    user = f.UserFactory(is_staff=True)
    yield user
    user.delete()


@pytest.fixture
def locations_data():
    yield [
        {
            'ID': 25,
            'Name': 'Girona'
        },
        {
            'ID': 26,
            'Name': 'Salt'
        },
    ]
