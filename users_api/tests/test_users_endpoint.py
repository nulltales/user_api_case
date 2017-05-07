import pytest
from rest_framework import reverse

from users_api.authentication import api_key_signer
from users_api.models import User


@pytest.fixture
def auth_client(api_client):
    api_client.credentials(HTTP_APIKEY=api_key_signer.sign('testing'))
    return api_client


@pytest.mark.django_db
def test_list_users(auth_client, mommy):
    users = mommy.make(
        User,
        _quantity=5
    )
    res = auth_client.get(reverse.reverse('user-list'))
    assert res.status_code == 200
    assert len(res.data) == 5
    assert res.data[0]['id'] == users[0].id


@pytest.mark.django_db
def test_create_user(auth_client):
    user_data = dict(
        first_name='Joe',
        last_name='Doe',
        email='jd@example.com',
    )
    res = auth_client.post(reverse.reverse('user-list'), user_data)
    assert res.status_code == 201
    assert res.data['first_name'] == user_data['first_name']
    assert res.data['last_name'] == user_data['last_name']
    assert res.data['email'] == user_data['email']


@pytest.mark.django_db
def test_create_user_unauthorized(api_client):
    user_data = dict(
        first_name='Joe',
        last_name='Doe',
        email='jd@example.com',
    )
    res = api_client.post(reverse.reverse('user-list'), user_data)
    assert res.status_code == 401
    assert res.data == {'detail': 'Authentication credentials were not provided.'}


@pytest.mark.django_db
def test_update_user(auth_client, mommy):
    user1 = mommy.make(
        User
    )
    user_data = dict(
        first_name='Joe',
        last_name='Doe',
        email='jd@example.com'
    )
    res = auth_client.put(reverse.reverse('user-detail', kwargs=dict(pk=user1.id)), user_data)
    assert res.status_code == 200
    assert res.data['first_name'] == user_data['first_name']
    assert res.data['last_name'] == user_data['last_name']
    assert res.data['email'] == user_data['email']

    res = auth_client.get(reverse.reverse('user-detail', kwargs=dict(pk=user1.id)))
    assert res.status_code == 200
    assert res.data['first_name'] == user_data['first_name']
    assert res.data['last_name'] == user_data['last_name']
    assert res.data['email'] == user_data['email']


@pytest.mark.django_db
def test_update_user_patch(auth_client, mommy):
    user1 = mommy.make(
        User
    )
    user_data = dict(
        first_name='Jane',
    )
    res = auth_client.patch(reverse.reverse('user-detail', kwargs=dict(pk=user1.id)), user_data)
    assert res.status_code == 200
    assert res.data['first_name'] == user_data['first_name']
    assert res.data['last_name'] == user1.last_name
    assert res.data['email'] == user1.email

    res = auth_client.get(reverse.reverse('user-detail', kwargs=dict(pk=user1.id)))
    assert res.status_code == 200
    assert res.data['first_name'] == user_data['first_name']
    assert res.data['last_name'] == user1.last_name
    assert res.data['email'] == user1.email



@pytest.mark.django_db
def test_update_user_patch(auth_client, mommy):
    user1 = mommy.make(
        User
    )

    res = auth_client.delete(reverse.reverse('user-detail', kwargs=dict(pk=user1.id)))
    assert res.status_code == 204

    res = auth_client.get(reverse.reverse('user-list'))
    assert res.status_code == 200
    assert len(res.data) == 0
