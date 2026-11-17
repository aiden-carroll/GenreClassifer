import numpy as np
import torch as pt

# In future Loss function with weights should be calcuated with
# weight = total tracks / (# of classes * tracks in that class)
def calculate_function(logits, y, class_weights: pt.Tensor | None = None):
    logp = pt.log_softmax(logits, dim=1)
    nll = -logp[pt.arange(len(y), device=y.device), y]
    if class_weights is None:
        return nll.mean()
    w = class_weights[y]
    return (w * nll).sum() / w.sum()