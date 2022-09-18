import datetime as dt
import streamlit as st
from firebase_admin import firestore
from google.cloud.firestore_v1.client import Client

from .base import BasePage
from smapi.models.user import User
from smapi.models.choice import Choice
from smapi.models.matching import Matching
from smapi.models.playerset import PlayerSet

# import streamlit_nested_layout
from smapi.const import hash_client, MatchingProblem, MailSendMode, TEXT_AREA_HEIGHT


class CreatePage(BasePage):
    def __init__(self, page_id, title):
        super().__init__(page_id, title)
        if "project_by_supervisor" not in st.session_state:
            st.session_state["project_by_supervisor"] = False

    @st.cache(hash_funcs={Client: hash_client}, allow_output_mutation=True)
    def connect_to_database(self, user: User):
        db = firestore.client()
        return db.collection(user.user_id)

    @st.cache(suppress_st_warning=True)
    def save(self, data: dict, publish: bool):
        if publish:
            data["published"] = True
            data["published_at"] = dt.datetime.now().isoformat()

        user = User.from_user_info(st.session_state["user_info"])
        data["created_by"] = user.user_id

        m = Matching.from_dict(data)
        user_ref = self.connect_to_database(user)
        user_ref.document("user").set(user.to_dict(), merge=True)
        user_ref.document("matching").set({m.matching_id: m.to_dict()}, merge=True)

    def render_by_m(self, m: dict):
        mp = m["problem"]
        gp = mp.groups()
        if mp == MatchingProblem.STABLE_ROOMMATES:
            st.write(gp[0])
            st.text_input("表示名", key="voter_name")
            st.text_area("選択肢", height=TEXT_AREA_HEIGHT, key="voter_choice")
            st.file_uploader(
                "選択肢 - CSVファイル",
                type="csv",
                accept_multiple_files=False,
                key="voter_csv",
                help="もしあればCSVファイルをアップロードしてください",
            )
            m["voters"] = PlayerSet(
                False,
                False,
                st.session_state["voter_name"],
                Choice.from_lines(st.session_state["voter_choice"] or st.session_state["voter_csv"]),
            )
        else:
            col23_condition = not st.session_state["project_by_supervisor"] and mp == MatchingProblem.STUDENT_ALLOCATION
            if col23_condition:
                col21, col22, col23 = st.columns([1, 1, 1])
            else:
                col21, col22 = st.columns([1, 1])

            with col21:
                st.write(gp[0])
                st.text_input("表示名", key="voter_name")
                st.text_area(
                    "選択肢,ランク" if mp == MatchingProblem.STUDENT_ALLOCATION else "選択肢",
                    height=TEXT_AREA_HEIGHT,
                    key="voter_choice",
                )
                st.file_uploader(
                    "選択肢 - CSVファイル",
                    type="csv",
                    accept_multiple_files=False,
                    key="voter_csv",
                    help="入力する代わりにCSVファイルをアップロードすることもできます",
                )
                m["voters"] = PlayerSet(
                    False,
                    mp == MatchingProblem.STUDENT_ALLOCATION,
                    st.session_state["voter_name"],
                    Choice.from_lines(st.session_state["voter_choice"] or st.session_state["voter_csv"]),
                )
            with col22:
                st.write(gp[1])
                st.text_input("表示名", key="candidate_name")
                st.text_area(
                    "選択肢,キャパシティ" if mp.has_capacity() else "選択肢", height=TEXT_AREA_HEIGHT, key="candidate_choice"
                )
                st.file_uploader(
                    "選択肢 - CSVファイル",
                    type="csv",
                    accept_multiple_files=False,
                    key="candidate_csv",
                    help="入力する代わりにCSVファイルをアップロードすることもできます",
                )
                m["candidates"] = PlayerSet(
                    mp.has_capacity(),
                    False,
                    st.session_state["candidate_name"],
                    Choice.from_lines(st.session_state["candidate_choice"] or st.session_state["candidate_csv"]),
                )
            if col23_condition:
                with col23:
                    st.write(gp[2])
                    st.text_input("表示名", key="subject_name")
                    st.text_area("選択肢,キャパシティ", height=TEXT_AREA_HEIGHT, key="subject_choice")
                    st.file_uploader(
                        "選択肢 - CSVファイル",
                        type="csv",
                        accept_multiple_files=False,
                        key="subject_csv",
                        help="入力する代わりにCSVファイルをアップロードすることもできます",
                    )
                    m["subjects"] = PlayerSet(
                        mp == MatchingProblem.STUDENT_ALLOCATION,
                        False,
                        st.session_state["subject_name"],
                        Choice.from_lines(st.session_state["subject_choice"] or st.session_state["subject_csv"]),
                    )
        return m

    def render(self):
        st.title("新規投票作成")

        m = st.session_state["m"] if "m" in st.session_state else {}

        st.subheader("基本設定")
        col11, col12, col13 = st.columns([2, 1, 1])
        m["name"] = col11.text_input("マッチング名称", key="name")
        m["expire_at"] = col12.date_input("投票締切時刻", help="23:59:59(JST)に締め切ります", key="expire").isoformat()
        m["mail_send_mode"] = col13.selectbox(
            "締切時メール通知対象",
            [MailSendMode.EVERYONE, MailSendMode.ONLY_AUTHOR, MailSendMode.NOBODY],
            format_func=lambda x: str(x),
            help="締め切り後にメール通知する対象を選択します",
        )

        m["problem"] = st.radio(
            "マッチング対象問題",
            [
                MatchingProblem.STABLE_ROOMMATES,
                MatchingProblem.STABLE_MARRIAGE,
                MatchingProblem.HOSPITAL_RESIDENT,
                MatchingProblem.STUDENT_ALLOCATION,
            ],
            format_func=lambda x: str(x),
            horizontal=True,
        )

        st.subheader("問題設定")
        st.warning("選択肢テキストエリアでは選択肢を改行区切りで入力してください")
        if m["problem"].has_capacity():
            st.warning("「選択肢,キャパシティ」とある記入欄にはカンマ区切りでキャパシティを入力してください")
        if m["problem"] == MatchingProblem.STUDENT_ALLOCATION:
            st.warning("卒業論文割当問題の学生側記入欄にはカンマ区切りで「学生の成績順位」を入力してください（カンマがない場合は自動的に昇順となります）")

        m = self.render_by_m(m)

        st.subheader("その他投票時設定")
        m["randomize"] = st.checkbox("投票ページの選択肢の初期配置をランダムにする", key="randomize")
        if m["problem"] == MatchingProblem.STUDENT_ALLOCATION:
            if st.checkbox("研究テーマは各教員に記入してもらう", key="project_by_supervisor"):
                m["input_subjects_by_candidates"] = True

        if "user_info" not in st.session_state:
            st.warning("Please login to continue")
            return

        col51, col52, _ = st.columns([1, 1, 8])

        if col51.button("保存", on_click=self.save, args=(m, False)):
            st.success("保存ボタンが押されました！")

        if col52.button("公開", on_click=self.save, args=(m, True)):
            st.success("公開ボタンが押されました！")
