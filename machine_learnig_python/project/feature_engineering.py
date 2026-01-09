import pandas as pd
from scipy.stats import kurtosis


def add_kurtosis_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add kurtosis-based features.
    """

    features = df.drop(columns=["target"])

    kurtosis_values = features.apply(
        lambda x: kurtosis(x, fisher=True)
    )

    for col in features.columns:
        df[f"{col}_kurtosis"] = kurtosis_values[col]

    return df
