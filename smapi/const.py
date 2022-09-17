from enum import Enum, IntEnum, auto

AUTH0_CLIENT_ID = "fcU1HuJJyqgGnQVwFrfKdh4LtX5o0FKD"
AUTH0_DOMAIN = "tk42.jp.auth0.com"


TEXT_AREA_HEIGHT = 220


class PageId(Enum):
    TOP = auto()
    INTRO = auto()
    CREATE = auto()
    MY_MATCHING = auto()
    MY_VOTE = auto()


class MatchingProblem(IntEnum):
    STABLE_ROOMMATES = 0
    STABLE_MARRIAGE = 1
    HOSPITAL_RESIDENT = 2
    STUDENT_ALLOCATION = 3

    def __str__(self):
        return ["安定ルームメイト問題", "安定結婚問題", "研修医配属問題", "卒業論文割当問題"][int(self)]

    def groups(self):
        if self == MatchingProblem.STABLE_ROOMMATES:
            return ["Roommates: ルームメイト"]
        elif self == MatchingProblem.STABLE_MARRIAGE:
            return ["Proposer: プロポーズ側(男性)", "Acceptor: 受け入れ側(女性)"]
        elif self == MatchingProblem.HOSPITAL_RESIDENT:
            return ["Proposer: プロポーズ側(研修医)", "Acceptor: 受け入れ側(病院)"]
        elif self == MatchingProblem.STUDENT_ALLOCATION:
            return ["Student: 学生側", "Supervisor: 教員側", "Project: 研究テーマ"]

    def has_capacity(self):
        return self != MatchingProblem.STABLE_MARRIAGE


class MailSendMode(IntEnum):
    NOBODY = 0
    ONLY_AUTHOR = 1
    EVERYONE = 2

    def __str__(self):
        return ["非通知", "作成者のみ", "投票者全員"][int(self)]
