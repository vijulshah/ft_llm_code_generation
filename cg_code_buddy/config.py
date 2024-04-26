import os
import sys
import os.path as osp

ROOT_PATH = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
sys.path.append(ROOT_PATH)

DATA_DIR = os.path.join(ROOT_PATH, 'data')
LOG_PATH = os.path.join(DATA_DIR, 'logs')
MODEL_PATH = os.path.join(DATA_DIR, 'ft_models', 'model_d')

TITLE_NAME = {'body': '👨‍💻 💬 Code Buddy'}
CAPTION = '🚀 This is a Python chatbot created by fine-tuning the open-source CodeLlama-7b-hf LLM model.'
AUTHOR_NAME = 'Vijul Shah'
AUTHOR_INFO = 'vijul1904@gmail.com'
INSTRUCTION_TEXT = '''
Generate a python code that appropriately completes the request based on the given instruction.

### Instruction:
    {instruction}

### Code:
'''
