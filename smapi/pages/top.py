import streamlit as st
from .base import BasePage


class TopPage(BasePage):
    def render(self):
        st.title("Sexytant Matching Proposal")
        st.write("全員がそれなりに幸せになれるマッチングを機械的に提案します")
        st.write("情報数学理論に基づき，お互いが今の相手よりも希望順位が高いペアが発生しないことが保証されます")
        st.write("キーワード：マーケットデザイン，グラフ理論，Gale-Shapleyアルゴリズム")
