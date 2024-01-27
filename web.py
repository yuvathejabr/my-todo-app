import streamlit as st
import functions

todos = functions.get_todos()


def add_todos():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.write_todos(todos)


st.title("My todo app")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="add new todo...",
              key="new_todo", on_change=add_todos)
