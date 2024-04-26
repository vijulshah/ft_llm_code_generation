import config
import streamlit as st
from gen_model import generate_code

def chat_area():
    
    if 'messages' not in st.session_state or st.session_state.messages == []:
        st.session_state.messages = [{'role': 'assistant', 'content': 'How may I assist you today?'}]
    
    for msg in st.session_state.messages:
        st.chat_message(msg['role']).write(msg['content'])

    # User-provided prompt
    if prompt := st.chat_input(placeholder='Message chat buddy...'):
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        st.chat_message('user').write(prompt)
        
        # Generate Python code based on instruction
        formated_instruction = config.INSTRUCTION_TEXT.format(instruction=prompt)
        generated_code = generate_code(instruction=formated_instruction)

        st.session_state.messages.append({'role': 'assistant', 'content': generated_code})
        st.chat_message('assistant').write(generated_code)
