import streamlit as st
from .base import BasePage


class TopPage(BasePage):
    def render(self):
        st.markdown(
            """
            # Sexytant Matching Proposal

            全員がそれなりに幸せになれるマッチングを機械的に提案します

            離散数学・ゲーム理論に基づくことで「安定マッチング」と呼ばれる一種の全体最適の状態を導きます

            キーワード：マーケットデザイン，ゲーム理論，Gale-Shapleyアルゴリズム（ノーベル経済学賞）

            ### 特徴
             - 投票ページを共有して，仲間内に安定的なマッチングを提案することができます
             - 4つのアルゴリズムに対応しています
               - 安定結婚問題
               - 研修医配属問題
               - 卒業論文割当問題
               - 安定ルームメイト問題

            ### 使い方
             - 投票を作成する際は「安定マッチングについて」ページで各種問題の理解を深め，どの問題と等価か見極めてください
             - 「新規投票作成」にて，投票を作成してください
             - 自分が作成した投票は「作成投票一覧」で確認できます
             - 自分に依頼された投票は「投票一覧」で確認できます
        """
        )
        st.image(
            "./smapi/assets/137069381_An_illust__of_stable_matching_on_bi_directed_graphs_solved_with_Gale_Shapley_algorithm.png"
        )
