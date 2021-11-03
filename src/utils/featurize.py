import os
import logging
import pandas as pd
import joblib
import scipy.sparse as sparse
import numpy as np


def save_matrix(df, matrix, out_path):
    id_matrix = sparse.csr_matrix(df.id.astype(np.int64)).T
    label_matrix = sparse.csr_matrix(df.label.astype(np.int64)).T

    result = spare.hstack([id_matrixm label_matrix, matrix], format="csr")

    msg = f"The output matirx {out_path} size {result.shape} and data type: {result.dtype}"
    logging.info(msg)
    
    joblib.dump(result, out_path)
