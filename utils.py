import os
import shutil
import tarfile
import requests
from pathlib import Path
import random

import numpy as np

import torch

def set_seed(seed):
  """
  Sets random seeds for reproducibility.
  """
  random.seed(seed)
  np.random.seed(seed)
  torch.manual_seed(seed)
  torch.cuda.manual_seed_all(seed)
  torch.backends.cudnn.deterministic = True
  torch.backends.cudnn.benchmark = False

def _download_url(url, file_path):
  response = requests.get(url, stream=True)
  response.raise_for_status()  # Raise an error for bad status codes
  with open(file_path, "wb") as file:
      for chunk in response.iter_content(chunk_size=8192):
          file.write(chunk)

def download_file(url, file_name, cache_dir="data", extract=True, force_download=False, archive_folder=None):
    # Ensure the cache directory exists
    os.makedirs(cache_dir, exist_ok=True)
    file_path = Path(cache_dir) / file_name

    # Download the file
    if not os.path.exists(file_path) or force_download:
      _download_url(url, file_path)
      print(f"File downloaded to: {file_path}")
    else:
      print(f"File already exists at: {file_path}")

    if extract:
      if file_name.endswith(".tar.gz"):
        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(path=cache_dir)
        print(f"File extracted to: {cache_dir}")
      else:
         shutil.unpack_archive(file_path, cache_dir)
      file_path = Path(cache_dir) / archive_folder if archive_folder is not None else Path(cache_dir)
    elif not extract and archive_folder is not None:
       file_path = Path(cache_dir) / archive_folder
       print(f"File already extracted to: {file_path}")

    return Path(file_path)