import streamlit as st
from .base import BasePage


class MyMatchingPage(BasePage):
    def render(self):
        st.title("作成投票一覧")
        st.write(
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        )
