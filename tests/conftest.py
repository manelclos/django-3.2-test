import pytest

from django.contrib.auth.models import Permission

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
def location_user(staff_user):
    permission = Permission.objects.get(codename='change_location')
    staff_user.user_permissions.add(permission)
    yield staff_user
    staff_user.user_permissions.remove(permission)
