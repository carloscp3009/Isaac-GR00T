from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="ami-iit-team-x/xbg",
    revision="manipulation-lang",
    repo_type="dataset",
    local_dir="demo_data/manipulation/",
)
