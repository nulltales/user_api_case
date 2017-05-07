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
