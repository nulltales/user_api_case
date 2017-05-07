"""
users_api URL Configuration
"""

import views

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    url(r'^$', get_swagger_view(title='Users API')),
    url(r'^users/?$', views.UsersListView.as_view(), name='users-list'),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetailView.as_view(), name='users-detail'),
]
