
from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_filters.backends import DjangoFilterBackend
from rest_framework import generics
from rest_framework_swagger import renderers
from users_api.authentication import api_key_signer, APIKeyAuthentication
from users_api.models import User
from users_api.serializers import UserSerializer


def welcome(request):
    return render(request, 'welcome.html', dict(api_key_token=api_key_signer.sign('mobiento')))


class UsersListView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing users.

    post:
    Create a new user instance.
    """
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'first_name': ['exact', 'iexact', 'startswith', 'contains'],
        'last_name': ['exact', 'iexact', 'startswith', 'contains'],
        'email': ['exact', 'iexact', 'startswith', 'contains']
    }


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Retrieve a specific user by ID.

    put:
    Replace a specific users data.

    patch:
    Update specific fields for a specific user.

    delete:
    Delete a specific user.
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SwaggerSchemaView(APIView):
    _ignore_model_permissions = True
    exclude_from_schema = True
    authentication_classes = []
    permission_classes = [AllowAny]
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator('Users API')
        schema = generator.get_schema(request=request)

        if not schema:
            raise exceptions.ValidationError(
                'The schema generator did not return a schema Document'
            )

        return Response(schema)
