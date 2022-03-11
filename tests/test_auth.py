import pytest

from app.storage.auth import AuthorizationService

auth_service = AuthorizationService()


def test_auth():
    auth_service.authorize('admin', 'SECRET')


def test_wrong():
    with pytest.raises(ValueError):
        auth_service.authorize('wrong', 'wrong')
