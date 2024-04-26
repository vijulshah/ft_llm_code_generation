import config
import streamlit as st

def how_to_use():
    st.markdown('''
        ## 👉 How to use Code Buddy? 👈\n
        Ask 💬 the buddy 👨‍💻 to write a python code for a specific task.\n\n
        '''
    )
    st.markdown('''
        **Example:**\n
        *Write a Function to find the nth Fibonacci number.*\n\n
        '''
    )
    st.markdown('---')

def clear_chat_history():
    st.session_state.messages = []
    st.session_state.current_message_id = 0
    st.session_state.formated_instruction = None

def about():
    st.markdown('# About')
    st.markdown(
        'Code Buddy generates a python code based on the given instruction.'
    )
    st.markdown('''
        Datasets used for fine tuning the model:\n
        - Hugging Face's `iamtarun/python_code_instructions_18k_alpaca` dataset & LLM Synthesized Datasets.\n\n
        LLM used for creating synthetic dataset: `meta.llama2-70b-chat-v1`.
        '''
    )
    st.markdown(f'Created by **{config.AUTHOR_NAME}** ({config.AUTHOR_INFO}). Checkout the [GitHub repo](https://github.com/vijulshah/ft_llm_code_generation.git)')
    
def sidebar():
    with st.sidebar:
        st.markdown('''
            <style>
            section[data-testid='stSidebar'][aria-expanded='true']{
                width: 25% !important;
            }
            section[data-testid='stSidebar'][aria-expanded='false']{
                width: 25% !important;
            }
            </style>
            ''', unsafe_allow_html=True
        )
        how_to_use()
        st.sidebar.button('Clear Chat History', on_click=clear_chat_history, use_container_width=True)
        st.markdown('---')
        about()
