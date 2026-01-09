import numpy as np
import pandas as pd
from sklearn.datasets import make_classification


def generate_synthetic_data(
    n_samples: int = 10000,
    n_features: int = 12,
    random_state: int = 42
) -> pd.DataFrame:
    """
    Generate synthetic classification data.
    """

    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=6,
        n_redundant=3,
        n_classes=2,
        weights=[0.7, 0.3],
        random_state=random_state
    )

    feature_names = [f"feature_{i}" for i in range(n_features)]
    df = pd.DataFrame(X, columns=feature_names)
    df["target"] = y

    return df
