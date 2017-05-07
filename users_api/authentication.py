
from django.core import signing
from rest_framework import exceptions, HTTP_HEADER_ENCODING
from django.utils.translation import ugettext_lazy as _
from rest_framework.authentication import TokenAuthentication
from datetime import timedelta
from django.core.signing import TimestampSigner
from django.utils.six import text_type

api_key_signer = TimestampSigner()


class APIKeyUser(object):

    def __init__(self, source):
        self.source = source

    @property
    def is_authenticated(self):
        return True

    def __repr__(self):
        return 'APIKey("{}")'.format(self.source)


def get_api_key_header(request):
    """
    Return request's 'ApiKey:' header, as a bytestring.
    """
    auth = request.META.get('HTTP_APIKEY', b'')
    if isinstance(auth, text_type):

        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


class APIKeyAuthentication(TokenAuthentication):

    def authenticate(self, request):
        auth = get_api_key_header(request)

        if not auth:
            return None

        try:
            token = auth.decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            value = api_key_signer.unsign(token, max_age=timedelta(hours=1))
        except (signing.BadSignature, signing.SignatureExpired):
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        return APIKeyUser(value), value
