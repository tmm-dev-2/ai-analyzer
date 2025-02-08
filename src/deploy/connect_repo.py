from huggingface_hub import Repository, HfApi

def connect_to_github():
    api = HfApi()
    
    repo = Repository(
        local_dir=".",
        clone_from="tmmdev/chart-analyzer",
        repo_type="space",
        use_auth_token=True
    )
    
    repo.git_remote_add_github(
        github_url="https://github.com/tmm-dev-2/ai-analyzer"
    )
    
    print("✨ Successfully connected to GitHub!")

if __name__ == "__main__":
    connect_to_github()
