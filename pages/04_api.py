import streamlit as st
import requests

st.title("🌐 外部API連携サンプル")
st.write("外部APIからデータを取得して表示するサンプルdです")

# ── ポケモン検索 ──────────────────────────────────
st.subheader("ポケモン検索(PokeAPI)")
pokemon = st.text_input("ポケモン名を英語で入力", placeholder="例: pikachu")

if st.button("検索"):
    if not pokemon:
        st.error("ポケモン名を入力してください")
    else:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            col1, col2 = st.columns(2)

            with col1:
                st.image(data["sprites"]["front_default"], caption=pokemon.capitalize())
            with col2:
                st.write(f"**ID:** {data['id']}")
                st.write(f"**高さ:** {data['height'] / 10} m")
                st.write(f"**重さ:** {data['weight'] / 10} kg")
                types = [t["type"]["name"] for t in data["types"]]
                st.write(f"**タイプ:** {', '.join(types)}")
        else:
            st.error("ポケモンが見つかりませんでした")
