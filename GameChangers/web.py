import streamlit as st
from code_editor import code_editor
import streamlit.components.v1 as components
import re
import main

st.title('The Game Changers 😎')
game = st.text_input('What is the game you would like to build? What will be the mechanics?')
if game is not None:
    code = main.make(game).raw
    patt = r'```python\n(.*?)```'
    code = re.search(patt, code, flags=re.DOTALL)
    print('code, ',code)
    st.write('### Try yourself first!')
    components.iframe("https://trinket.io/embed/python/4b7b7fd41d", width=1100, height=400)
    st.write('Code for help...')
    user_code = code_editor(code.string[10:-3], lang='python')
