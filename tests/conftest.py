import uuid

import pytest
from rest_framework.authtoken.models import Token


@pytest.fixture
def password():
   return 'strong-test-password'


@pytest.fixture
def user_fixture(db, django_user_model, password):
   return django_user_model.objects.create_user(username=str(uuid.uuid4()), password=password)


@pytest.fixture
def get_or_create_token(db, user_fixture):
   token, _ = Token.objects.get_or_create(user=user_fixture)
   return token


@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()


@pytest.fixture
def api_client_with_credentials(db, user_fixture, api_client):
   api_client.force_authenticate(user=user_fixture)
   yield api_client
   api_client.force_authenticate(user=None)

