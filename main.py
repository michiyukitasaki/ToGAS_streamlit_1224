import streamlit as st
import requests

st.title("体温/体重入力")

# ユーザー入力
temperature = st.number_input("体温", value=None)
weight = st.number_input("体重", value=None)

# 送信ボタン
if st.button("送信"):
    # POSTリクエストを実行するための条件を追加
    if temperature:
        # GASのURL for temperature
        url_temperature = "https://script.google.com/macros/s/AKfycbwNeewcT7PF5NjTpMml9PIDXJzFCL-079ha9LoZQiXYzaT-0fN0jxdL5UpFYnhVQOQU/exec"
        data_temp = {"temperature": temperature}
        response_for_temp = requests.post(url_temperature, json=data_temp)
        st.write("体温: " + response_for_temp.text)

    if weight:
        # GASのURL for weight
        url_weight = "https://script.google.com/macros/s/AKfycbx7kOQbcU2vMjyCb9EWH3Q9O0sMyXTJxmo6AaMMOHGmlbuQvhq6CfAcRftUOjKC8JiR/exec"
        data_weight = {"weight": weight}
        response_for_weight = requests.post(url_weight, json=data_weight)
        st.write("体重: " + response_for_weight.text)
