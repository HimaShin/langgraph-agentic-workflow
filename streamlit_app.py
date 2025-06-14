import streamlit as st
from agents.plan_agent import split_into_tasks
from agents.tool_agent import solve_task

st.set_page_config(page_title="LangGraph Agentic Workflow", layout="wide")

st.title("🤖 LangGraph Agentic Workflow")

query = st.text_area("📝 Enter your main query:")

if st.button("Run Workflow"):
    if not query.strip():
        st.warning("Please enter a valid query.")
    else:
        st.subheader("📋 Sub-Tasks")
        tasks = split_into_tasks(query)
        for i, task in enumerate(tasks, 1):
            st.markdown(f"**{i}. {task}**")

        st.subheader("✅ Results")
        for task in tasks:
            result = solve_task(task)
            st.markdown(f"**{task}** → {result}")
