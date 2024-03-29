from typing import Tuple

import numpy as np


def discrete_bayes(
    # the prior: shape=(n,)
    pr: np.ndarray,
    # the conditional/likelihood: shape=(n, m)
    cond_pr: np.ndarray,
) -> Tuple[
    np.ndarray, np.ndarray
]:  # the new marginal and conditional: shapes=((m,), (m, n))
    """Swap which discrete variable is the marginal and conditional."""
    # Pr(s_k | s_k-1, z_k-1)*Pr(s_k-1 | z_k-1)
    
    joint = cond_pr @ pr   # TDOO 
    marginal = joint.sum(axis=0) # TODO

    # Take care of rare cases of degenerate zero marginal,
    if marginal[None]>0:
        conditional = np.divide(joint,marginal)# TODO
    else:
        conditional = None
        print("marginal is zero")

    # flip axes?? (n, m) -> (m, n)
    conditional = conditional.T

    # optional DEBUG
    assert np.all(
        np.isfinite(conditional)
    ), f"NaN or inf in conditional in discrete bayes"
    assert np.all(
        np.less_equal(0, conditional)
    ), f"Negative values for conditional in discrete bayes"
    assert np.all(
        np.less_equal(conditional, 1)
    ), f"Value more than on in discrete bayes"

    assert np.all(np.isfinite(marginal)), f"NaN or inf in marginal in discrete bayes"

    return marginal, conditional
