from .app import MultiPageApp
from .const import PageId
from .pages.base import BasePage

from .pages.top import TopPage
from .pages.create import CreatePage
from .pages.my_matching import MyMatchingPage
from .pages.my_vote import MyVotePage


def init_pages() -> list[BasePage]:
    pages = [
        TopPage(page_id=PageId.TOP, title="トップ"),
        CreatePage(page_id=PageId.CREATE, title="新規投票作成"),
        MyMatchingPage(page_id=PageId.MY_MATCHING, title="作成投票一覧"),
        MyVotePage(page_id=PageId.MY_VOTE, title="投票一覧"),
    ]
    return pages


def init_app(pages: list[BasePage]) -> MultiPageApp:
    app = MultiPageApp(pages)
    return app
