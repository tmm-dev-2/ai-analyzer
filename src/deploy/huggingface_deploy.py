from huggingface_hub import HfApi, create_repo, login
import os
from dotenv import load_dotenv

load_dotenv()

def deploy_to_huggingface():
    TOKEN = os.getenv('HF_TOKEN')
    login(token=TOKEN)
    api = HfApi()
    
    space_name = "tmmdev/chart-analyzer"
    
    space = create_repo(
        repo_id=space_name,
        token=TOKEN,
        repo_type="space",
        space_sdk="gradio",
        private=False
    )
    
    print(f"✨ Space created: https://huggingface.co/spaces/{space_name}")
