import streamlit as st
import json
import os
import time

st.set_page_config(
    page_title="AI Factory Command Dashboard",
    page_icon="🤖",
    layout="wide"
)

def load_blueprint():
    if os.path.exists("dependency_graph.json"):
        with open("dependency_graph.json", "r") as f:
            return json.load(f)
    return None

data = load_blueprint()

if not data:
    st.error("Missing critical configuration blueprint file: 'dependency_graph.json'. Please check root directories.")
    st.stop()

# Title Bar Layout
st.title("🤖 Multi-Agent Software Factory Console")
st.subheader("Autonomous Repository Matrix & Quality Lockdown System")

# High Level Global Parameters
col1, col2, col3 = st.columns(3)
with col1:
    status_colors = {
        "INITIALIZING_SWARM": "🔵 Initializing Factory Channels",
        "BUILDING_REPOS": "⚡ Swarm Active - Generating Codebases",
        "LOCKED_AND_LIVE": "🟢 System 100% Fully Verified & Locked"
    }
    st.metric(
        label="System Factory Core State", 
        value=status_colors.get(data["system_status"], data["system_status"])
    )

with col2:
    st.metric(
        label="Unified Master Code Test Score", 
        value=f"{data['global_score']}%"
    )

with col3:
    is_ready = "READY" if data["global_score"] == 100 else "HOLD - COMPILING"
    st.metric(label="Production Release Certification Gate", value=is_ready)

st.markdown("---")

# Draw Modules State Panel
st.header("📦 Standalone System Modules Matrix")
mod_cols = st.columns(len(data["modules"]))

for idx, (mod_id, mod_info) in enumerate(data["modules"].items()):
    with mod_cols[idx]:
        with st.container(border=True):
            st.subheader(mod_info["friendly_name"])
            
            # Label badges mapping
            status = mod_info["status"]
            if status == "PENDING":
                st.info("Status: 🔘 Pending Build")
            elif status == "IN_PROCESS":
                st.warning("Status: ⚡ Writing Code...")
            elif status == "HEALING_CODE":
                st.error("Status: 🩺 Fixing Bugs...")
            elif status == "LOCKED":
                st.success("Status: 🔒 Fully Verified & Locked")
                
            st.progress(mod_info["progress"] / 100)
            st.metric(label="Module Test Suite Score", value=f"{mod_info['test_score']}%")
            
            st.markdown("**Expected Artifact Scope:**")
            for file in mod_info["files"]:
                st.caption(f"📄 `{file}`")
                
            if mod_info["last_error"]:
                st.markdown("---")
                st.caption("🚨 **Latest Execution Catch:**")
                st.code(mod_info["last_error"], language="bash")

st.markdown("---")

# Real Time Swarm Events Console
st.header("📜 Live Swarm Agent Real-Time Operations Log")
st.text_area(
    label="Orchestrator Automation Activity Engine Log",
    value="\n".join(data["logs"]),
    height=300,
    disabled=True
)

# JavaScript Triggered Automated Rerun Injector (keeps dashboard feeling fast and dynamic)
time.sleep(1)
st.rerun()
