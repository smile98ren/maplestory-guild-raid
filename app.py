import streamlit as st
import pandas as pd

st.title("楓之谷公會副本組隊系統")

boss_list = ["困難史烏","困難露希妲","困難威爾","困難戴米安"]

job_list = [
"英雄","聖騎士","黑騎士",
"夜使者","暗影神偷","影武者",
"箭神","神射手",
"主教","冰雷","火毒"
]

if "teams" not in st.session_state:
    st.session_state.teams = []

menu = st.sidebar.selectbox("選單",["查看隊伍","建立隊伍"])

if menu == "建立隊伍":

    st.header("建立副本隊伍")

    boss = st.selectbox("副本",boss_list)
    team = st.text_input("隊伍名稱")

    if st.button("建立"):
        st.session_state.teams.append({
            "boss":boss,
            "team":team,
            "members":[]
        })

        st.success("隊伍建立成功")

if menu == "查看隊伍":

    for t in st.session_state.teams:

        st.subheader(t["boss"]+" - "+t["team"])

        st.write("人數:",len(t["members"]),"/6")

        if len(t["members"]) < 6:

            name = st.text_input("角色ID",key=t["team"])
            job = st.selectbox("職業",job_list,key=t["team"]+"job")

            if st.button("加入",key=t["team"]+"join"):

                t["members"].append({
                    "name":name,
                    "job":job
                })

                st.success("加入成功")

        for m in t["members"]:
            st.write(m["name"],m["job"])
