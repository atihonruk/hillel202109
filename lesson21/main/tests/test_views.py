from unittest.mock import patch
import pytest

from mixer.backend.django import mixer
# 1. RequestFactory (isolated)
# 2. Client         (full flow)

from ..views import index

pytestmark = pytest.mark.django_db


@pytest.fixture
def search_engine():
    print('Set Up')
    # set up
    yield object()
    # tear down
    print('Tear down')


def test_index_rf(rf):
    req = rf.get('/')
    # with Class-based views:
    # resp = IndexView.as_view()(req)
    resp = index(req)
    assert resp.status_code == 200



test_key = 'asdfg'
test_url = 'https://www.python.org/'

    
def test_index_client(client):
    resp = client.get('/')
    assert resp.status_code == 200



def test_redirect(client):
    
    # make key: url pair
    with patch('main.models.gen_key', lambda: test_key):
        resp = client.post('/', {'url': test_url})
        assert resp.status_code == 200
    
        # make sure key redirects to url
        resp = client.get('/' + test_key)
        assert resp.status_code == 302
        assert resp.url == test_url


def test_post_client_is_not_authenticated(client):
    resp = client.post('/', {'url': test_url})
    assert resp.status_code == 302
    assert 'login' in resp.url 


def test_post_rf_is_authenticated(rf):
    req = rf.post('/', {'url': test_url})
    user = mixer.blend('auth.User')
    req.user = user

