from huggingface_hub import HfApi, login
from dotenv import load_dotenv
import os

def update_space_repo():
    load_dotenv()
    api = HfApi()
    login(token=os.getenv('HF_TOKEN'))
    
    api.upload_folder(
        folder_path=".",
        repo_id="tmmdev/chart-analyzer",
        repo_type="space"
    )
    
    print("✨ Space updated successfully!")

if __name__ == "__main__":
    update_space_repo()
