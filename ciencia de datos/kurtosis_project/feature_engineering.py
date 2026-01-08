from scipy.stats import kurtosis

def calcular_kurtosis(df):
    return (
        df.groupby("dia")["monto"]
        .apply(lambda x: kurtosis(x, fisher=True))
        .reset_index(name="kurtosis")
    )
