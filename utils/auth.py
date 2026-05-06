import streamlit as st

# サンプルユーザー
# 実際はDBやsecretsファイルで管理してください
USERS = {"admin": "password123", "user01": "password456"}


def login():
    """ログインフォームを表示し、認証状態を管理する"""

    # セッションに logged_in がなければ初期化
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    if st.session_state.logged_in:
        return True

    st.subheader("🔐 ログイン")
    username = st.text_input("ユーザー名")
    password = st.text_input("パスワード", type="password")

    if st.button("ログイン"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("ユーザー名またはパスワードが間違っています")
    return False


def logout():
    """ログアウトする"""
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.rerun()
