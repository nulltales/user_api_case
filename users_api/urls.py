"""
users_api URL Configuration
"""

import views

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    url(r'^$', views.welcome),
    url(r'^schema/?$', views.SwaggerSchemaView.as_view()),
    url(r'^users/?$', views.UsersListView.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetailView.as_view(), name='user-detail'),
]
