from transformers import AutoTokenizer
from gen_model import load_model

def initialize_session_states(session_state):

    if 'tokenizer' not in session_state:
        tokenizer_configs = {
            'model_max_length': 256,  # Maximum sequence length supported by the tokenizer
            'pretrained_model_name_or_path': 'codellama/CodeLlama-7b-hf'  # Name or path of the pre-trained tokenizer model
        }
        tokenizer = AutoTokenizer.from_pretrained(**tokenizer_configs)
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.padding_side = 'right'
        session_state.tokenizer = tokenizer
        
    # load the selected model
    if 'model' not in session_state:
        session_state.model = load_model()

    # previous conversation as message objects
    if 'messages' not in session_state:
        session_state.messages = []
    
    # text input from user which is formated to send directly into the model
    if 'formated_instruction' not in session_state:
        session_state.formated_instruction = None
