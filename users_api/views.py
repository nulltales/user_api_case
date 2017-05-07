from django.http import HttpResponse
from rest_framework import generics

from users_api.models import User
from users_api.serializers import UserSerializer

counter = 1


def index(request):
    global counter
    counter += 1
    return HttpResponse('Hello world! ' + str(counter))


class UsersListView(generics.ListCreateAPIView):

    authentication_classes = ()
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = ()
    serializer_class = UserSerializer
    queryset = User.objects.all()
