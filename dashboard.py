import streamlit as st
import json
import os
import time

st.set_page_config(page_title="AI Factory Studio Control Center", layout="wide")
st.title("🤖 Multi-Agent Software Factory Core")

if os.path.exists("dependency_graph.json"):
    with open("dependency_graph.json", "r") as f:
        data = json.load(f)
    
    col1, col2 = st.columns(2)
    col1.metric("Unified Factory Architecture State", data["system_status"])
    col2.metric("Master Global Verification Score", f"{data['global_score']}%")
    
    st.write("---")
    st.subheader("Isolated Target Module States")
    cols = st.columns(4)
    
    for idx, (mid, info) in enumerate(data["modules"].items()):
        with cols[idx]:
            st.info(f"**{info['friendly_name']}**")
            st.write(f"Build Stage: `{info['status']}`")
            st.progress(info["progress"] / 100)
            st.caption(f"Code Quality Validation: {info['test_score']}%")
            if info["last_error"]:
                st.error(info["last_error"])
                
    st.write("---")
    st.subheader("Asynchronous Production Pipeline Logs")
    st.text_area("Live Events Stream", value="\n".join(data["logs"]), height=200)
else:
    st.error("dependency_graph.json mapping schema not found in local context path.")

time.sleep(1.5)
st.rerun()
