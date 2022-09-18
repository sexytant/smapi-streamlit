import datetime as dt
import streamlit as st
from firebase_admin import firestore
from google.cloud.firestore_v1.client import Client

from .base import BasePage
from smapi.models.user import User
from smapi.const import hash_client, MatchingProblem, MailSendMode, TEXT_AREA_HEIGHT


class MyMatchingPage(BasePage):
    @st.cache(hash_funcs={Client: hash_client}, allow_output_mutation=True)
    def connect_to_database(self, user: User):
        db = firestore.client()
        return db.collection(user).document("matching")

    def sort_data(self, ref):
        doc = ref.get()
        if doc.exists:
            return {k: v for k, v in sorted(doc.to_dict().items(), key=lambda x: x[1]["created_at"])}
        else:
            return None

    def render(self):
        st.title("作成投票一覧")

        if "user_info" not in st.session_state:
            st.warning("Please login to continue")

        st.write(
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        )
