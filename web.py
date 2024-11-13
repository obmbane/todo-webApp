import streamlit as st
import functions

from functions import get_todos

todos = functions.get_todos()

def add_new_todo():
    todo =st.session_state['new_todo_box'].capitalize()
    todos.append(todo+'\n')
    functions.write_todos(todos)


st.title('Todo App')
st.subheader('Managing Your Busy Schedule is Now Easier Than Ever')
st.write('Ready To Get Started? Capture Your To-Do list below!')

st.text_input(label='',placeholder='Add New To Do Item...',on_change=add_new_todo, key='new_todo_box')

for num, item in enumerate(todos):
    checkbox = st.checkbox(item,key=item)
    print(checkbox)
    if checkbox:
        todos.pop(num)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()

