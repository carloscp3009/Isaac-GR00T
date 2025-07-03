from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="ami-iit/component_X_lerobot",
    repo_type="dataset",
    local_dir="./demo_data/",
)
