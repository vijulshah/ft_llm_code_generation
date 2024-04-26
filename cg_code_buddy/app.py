import config
import streamlit as st
from chat import chat_area
from sidebar import sidebar
from session import initialize_session_states

def main():
    
    st.set_page_config(layout="wide")
    st.title(**config.TITLE_NAME)
    st.caption(config.CAPTION)
    
    initialize_session_states(session_state=st.session_state)
    sidebar()
    chat_area()
    
if __name__ == "__main__":
    main()

# execute bash command: streamlit run app.py
