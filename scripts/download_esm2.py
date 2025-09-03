#!/usr/bin/env python
"""
Download ESM2 models from Hugging Face into ./models/
Usage:
    python scripts/download_esm2.py esm2_t6_8M_UR50D
    python scripts/download_esm2.py esm2_t33_650M_UR50D
"""
import sys
from pathlib import Path
from huggingface_hub import snapshot_download

# Map shorthand names to full repo IDs
ESM2_MODELS = {
    "esm2_t6_8M_UR50D": "facebook/esm2_t6_8M_UR50D",
    "esm2_t12_35M_UR50D": "facebook/esm2_t12_35M_UR50D",
    "esm2_t30_150M_UR50D": "facebook/esm2_t30_150M_UR50D",
    "esm2_t33_650M_UR50D": "facebook/esm2_t33_650M_UR50D",
}

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ESM2_MODELS:
        print("Usage: python scripts/download_esm2.py <model_key>")
        print("Choices:", ", ".join(ESM2_MODELS.keys()))
        sys.exit(1)

    key = sys.argv[1]
    repo_id = ESM2_MODELS[key]

    out_dir = Path("models") / key.replace("/", "__")
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Downloading {repo_id} into {out_dir} ...")
    snapshot_download(
        repo_id,
        local_dir=out_dir,
        local_dir_use_symlinks=False,  # ensure real files, not symlinks
        resume_download=True,
    )
    print(f"Done. Model available at {out_dir}")

if __name__ == "__main__":
    main()

