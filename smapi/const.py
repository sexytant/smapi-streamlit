from enum import Enum, auto

AUTH0_CLIENT_ID = "fcU1HuJJyqgGnQVwFrfKdh4LtX5o0FKD"
AUTH0_DOMAIN = "tk42.jp.auth0.com"


class PageId(Enum):
    TOP = auto()
    CREATE = auto()
    MY_MATCHING = auto()
    MY_VOTE = auto()
