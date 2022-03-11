from typing import Dict

import pandas as pd

from app.entities.user import UserModel

ADMIN = UserModel(id=0, login='admin', password='SECRET')


class AuthorizationService:
    def __init__(self):
        self._users: Dict[str, UserModel] = {'admin': ADMIN}
        self._user_data = {}

    def add_user_data(self, user_id, data: pd.DataFrame):
        self._user_data[user_id] = data

    def authorize(self, login: str, password: str) -> UserModel:
        user = self._users.get(login, None)
        if user is None or user.password != password:
            raise ValueError
        return user
