import streamlit as st
import requests


st.title("体温記録アプリ")

# ユーザー入力
date = st.text_input("日付", value="")
temperature = st.text_input("体温", value="")

# 送信ボタン
if st.button("送信"):
    # GASのURL
    url = "https://script.google.com/macros/s/AKfycbwNeewcT7PF5NjTpMml9PIDXJzFCL-079ha9LoZQiXYzaT-0fN0jxdL5UpFYnhVQOQU/exec"

    # データの収集
    data = {"date": date, "temperature": temperature}

    # POSTリクエスト
    response = requests.post(url, json=data)

    # 結果の表示
    st.write(response.text)


# ガター内の緑色のボタンを押すとスクリプトを実行します。


# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
