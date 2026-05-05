import streamlit as st

st.title("📝 フォームサンプル")

# ── 入力フォーム ──────────────────────────────────
st.subheader("情報を入力してください")

name = st.text_input("名前")
age = st.number_input("年齢", min_value=0, max_value=120, step=1)
lang = st.selectbox("得意な言語", ["Python", "JavaScript", "Java", "その他"])
memo = st.text_area("一言メモ")

# ── 送信ボタン ────────────────────────────────────
if st.button("送信"):
    if not name:
        st.error("名前を入力してください！")
    else:
        st.success("送信完了！")
        st.write(f"**名前:** {name}")
        st.write(f"**年齢:** {age}")
        st.write(f"**得意な言語:** {lang}")
        st.write(f"**メモ:** {memo}")
