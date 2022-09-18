import streamlit as st
from .base import BasePage
from smapi.models.user import User


class MyVotePage(BasePage):
    def render(self):
        st.title("投票一覧")

        if "user_info" not in st.session_state:
            st.warning("Please login to continue")
            return

        st.write(
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        )
