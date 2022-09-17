import streamlit as st
from .base import BasePage


class IntroPage(BasePage):
    def render(self):
        st.title("安定マッチングについて学ぶ")
        st.markdown(
            """
        ## 安定結婚問題
         - 2グループ(例：男と女)のそれぞれが1:1のペアリングを望む時，各々の選好を考慮する
         - 「安定マッチング」であるとはお互いが今の相手よりも希望順位が高いペアが発生しないこと
         - Gale-Shapleyのアルゴリズムにより，安定マッチングであることが保証される
         - Gale-Shapleyのアルゴリズムは「男女平等ではない」．（男性最適安定マッチングと女性最適安定マッチングがある）
         - 安定マッチングは複数存在しうる
         - 安定マッチング≠不満を最小化するマッチング
         - プロポーズ側には耐戦略性がある（選好順序リストに嘘を書いても，より良い相手をマッチすることはない）
        """
        )
        st.image("./smapi/assets/stable_marriage_01.png")
        st.markdown(
            """
        ## 研修医配属問題
         - 選好順序リストが不完全な1対多の配属問題
         - [医師臨床研修マッチング協議会](https://www.jrmp.jp/)の[組合せ決定のアルゴリズム図解](https://jrmp2.s3-ap-northeast-1.amazonaws.com/distribution/matching.html)が詳しい
        """
        )
        st.image("./smapi/assets/hospital_resident_01.png")
        st.markdown(
            """
        ## 卒業論文割当問題

        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        ## 安定ルームメイト問題

        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

        ----
        """
        )
        st.write("参考：早稲田大学基幹理工学部応用数理学科准教授 早水桃子氏の動画")
        st.video("https://www.youtube.com/watch?v=ib8jjBIlYqw")
