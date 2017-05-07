import pytest
from rest_framework import exceptions

from users_api.authentication import APIKeyAuthentication, api_key_signer


def test_auth_not_available(api_rf):
    r = api_rf.get('/')
    r.data = {}

    # Authenticators should return None if not possible to perform authentication. In this case missing header.
    assert APIKeyAuthentication().authenticate(r) is None


def test_auth_invalid_token(api_rf):

    r = api_rf.get('/', HTTP_APIKEY='foo')
    with pytest.raises(exceptions.AuthenticationFailed) as e:
        APIKeyAuthentication().authenticate(r)
    assert e.value.detail == 'Invalid token.'


def test_auth_valid_token(api_rf):
    valid_token = api_key_signer.sign('mobiento')
    r = api_rf.get('/', HTTP_APIKEY=valid_token)
    assert APIKeyAuthentication().authenticate(r)[1] == 'mobiento'


def test_auth_expired_token(api_rf, freeze_time):
    with freeze_time('1999-01-01'):
        expired_token = api_key_signer.sign('mobiento')

    with pytest.raises(exceptions.AuthenticationFailed) as e:
        r = api_rf.get('/', HTTP_APIKEY=expired_token)
        APIKeyAuthentication().authenticate(r)
    assert e.value.detail == 'Invalid token.'
