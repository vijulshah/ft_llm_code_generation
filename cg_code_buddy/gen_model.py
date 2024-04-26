import torch
import transformers
import streamlit as st
from peft import AutoPeftModelForCausalLM
from transformers import BitsAndBytesConfig

from config import MODEL_PATH 

def load_model():

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,  # Loads the pre-trained model in 4-bit quantization mode
        bnb_4bit_use_double_quant=True,  # Uses double quantization in 4-bit mode
        bnb_4bit_quant_type='nf4',  # Specifies the quantization type as 'nf4'
        bnb_4bit_compute_dtype=torch.bfloat16  # Specifies the compute datatype as torch.bfloat16
    )

    model = AutoPeftModelForCausalLM.from_pretrained(
        pretrained_model_name_or_path=MODEL_PATH,
        low_cpu_mem_usage=True,         # Reduce CPU memory usage
        torch_dtype=torch.float16,      # Use 16-bit floating point precision
        quantization_config=bnb_config  # Specifies the quantization configuration
    )

    return model

def generate_code(instruction):
    tokenizer = st.session_state.tokenizer
    inputs = tokenizer(instruction, return_tensors='pt')  # Tokenizing instruction
    st.session_state.model.eval()
    output_tokens = st.session_state.model.generate(inputs['input_ids'], max_new_tokens=256, pad_token_id=tokenizer.eos_token_id)[0]  # Generating output tokens
    predicted_output = tokenizer.decode(output_tokens, skip_special_tokens=True)  # Decoding output tokens
    return predicted_output
