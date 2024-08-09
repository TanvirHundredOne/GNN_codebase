import numpy as np

import pandas as pd

import torch
import torch.nn as nn
import torch.nn.functional as F
import dgl
from dgl.data import CoraGraphDataset

import requests
import zipfile
import io
from sklearn.preprocessing import LabelEncoder


def main(dataset="cora"):
    if dataset == "cora":
        src_dst_df, node_feat_df = get_processed_cora_dataset()


if __name__ == "__main__":
    main()
