import os

from instagrapi.types import UserShort

from instagrapi import Client


class InstagramClient:
    def __init__(self):
        self.client = Client()

    def authenticate(self):
        self.client.login(os.environ['INSTAGRAM_USER'], os.environ['INSTAGRAM_PASSWORD'])

    def get_user_id(self, account: str) -> str:
        return self.client.user_id_from_username(account)

    def get_followers(self, account: str) -> dict[str, UserShort]:
        user_pk = self.get_user_id(account)
        return self.client.user_followers(user_pk)



