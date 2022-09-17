import streamlit as st
from .base import BasePage
import streamlit_nested_layout
from smapi.const import MatchingProblem, MailSendMode, TEXT_AREA_HEIGHT


class CreatePage(BasePage):
    def __init__(self, page_id, title):
        super().__init__(page_id, title)
        if "project_by_supervisor" not in st.session_state:
            st.session_state["project_by_supervisor"] = False

    def render_by_mp(self, mp: MatchingProblem):
        gp = mp.groups()
        if mp == MatchingProblem.STABLE_ROOMMATES:
            st.write(gp[0])
            st.text_input("表示名", key="proposor_name")
            st.text_area("選択肢", height=TEXT_AREA_HEIGHT, key="proposer_choice")
            st.file_uploader(
                "CSVファイル", type="csv", accept_multiple_files=False, key="proposer_csv", help="もしあればCSVファイルをアップロードしてください"
            )
        else:
            col23_condition = not st.session_state["project_by_supervisor"] and mp == MatchingProblem.STUDENT_ALLOCATION
            if col23_condition:
                col21, col22, col23 = st.columns([1, 1, 1])
            else:
                col21, col22 = st.columns([1, 1])

            with col21:
                st.write(gp[0])
                st.text_input("表示名", key="proposor_name")
                st.text_area("選択肢", height=TEXT_AREA_HEIGHT, key="proposer_choice")
                st.file_uploader(
                    "CSVファイル",
                    type="csv",
                    accept_multiple_files=False,
                    key="proposer_csv",
                    help="入力する代わりにCSVファイルをアップロードすることもできます",
                )
            with col22:
                st.write(gp[1])
                st.text_input("表示名", key="acceptor_name")
                st.text_area(
                    "選択肢,キャパシティ" if mp.has_capacity() else "選択肢", height=TEXT_AREA_HEIGHT, key="acceptor_choice"
                )
                st.file_uploader(
                    "CSVファイル",
                    type="csv",
                    accept_multiple_files=False,
                    key="acceptor_csv",
                    help="入力する代わりにCSVファイルをアップロードすることもできます",
                )
            if col23_condition:
                with col23:
                    st.write(gp[2])
                    st.text_input("表示名", key="medium_name")
                    st.text_area("選択肢,キャパシティ", height=TEXT_AREA_HEIGHT, key="medium_choice")
                    st.file_uploader(
                        "CSVファイル",
                        type="csv",
                        accept_multiple_files=False,
                        key="medium_csv",
                        help="入力する代わりにCSVファイルをアップロードすることもできます",
                    )

    def render(self):
        st.title("新規投票作成")
        st.subheader("基本設定")
        col11, col12, col13 = st.columns([2, 1, 1])
        col11.text_input("マッチング名称", key="name")
        col12.date_input("投票締切時刻", help="23:59:59(JST)に締め切ります", key="expire")
        col13.selectbox(
            "締切時メール通知対象",
            [MailSendMode.EVERYONE, MailSendMode.ONLY_AUTHOR, MailSendMode.NOBODY],
            format_func=lambda x: str(x),
            help="締め切り後にメール通知する対象を選択します",
        )

        mp = st.radio(
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
        st.warning("テキストエリアでは選択肢を改行区切りで入力してください．「選択肢,キャパシティ」とある場合はカンマ区切りでキャパシティを入力してください")

        self.render_by_mp(mp)

        st.subheader("その他投票時設定")
        st.checkbox("選択肢の初期配置をランダムにする", key="randomize")
        if mp == MatchingProblem.STUDENT_ALLOCATION:
            st.checkbox("研究テーマは各教員に記入してもらう", key="project_by_supervisor")

        col51, col52, _ = st.columns([1, 1, 8])

        if col51.button("保存"):
            st.success("保存ボタンが押されました！")

        if col52.button("公開"):
            st.success("公開ボタンが押されました！")
