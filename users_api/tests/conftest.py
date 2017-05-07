import pytest
from pytest_django.lazy_django import skip_if_no_django


@pytest.fixture
def api_rf():
    """
    APIRequestFactory instance
    see http://www.django-rest-framework.org/api-guide/testing
    """
    skip_if_no_django()

    from rest_framework.test import APIRequestFactory

    return APIRequestFactory()


@pytest.fixture
def api_client():
    """
    APIClient instance
    see http://www.django-rest-framework.org/api-guide/testing#apiclient
    """
    skip_if_no_django()

    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def freeze_time():
    """
    freeze_time instance
    Useful for testing stuff depending on datetime.utcnow()
    see https://github.com/spulec/freezegun
    """
    from freezegun import freeze_time

    return freeze_time


@pytest.fixture
def mommy():
    """
    ModelMommy instance
    see http://model-mommy.readthedocs.org/en/latest/index.html
    """

    from model_mommy import mommy

    return mommy
