import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


def test_key_generated():
    obj = mixer.blend("main.Url")
    assert len(obj.key) == 5, 'Should contain 5 symbols'
