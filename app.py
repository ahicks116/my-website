import streamlit as st

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📝 To-Do List App")

# Add new task
with st.form("add_task_form"):
    new_task = st.text_input("Enter a new task")
    submitted = st.form_submit_button("Add Task")
    if submitted and new_task.strip():
        st.session_state.tasks.append(new_task.strip())
        st.success(f"Added task: {new_task}")

# Display tasks
st.subheader("Your Tasks:")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            st.write(f"{i+1}. {task}")
        with col2:
            if st.button("❌", key=f"del_{i}"):
                st.session_state.tasks.pop(i)
                st.experimental_rerun()
else:
    st.info("Your to-do list is empty.")
