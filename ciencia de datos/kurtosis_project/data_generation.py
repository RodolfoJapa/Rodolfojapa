import numpy as np
import pandas as pd

def generar_transacciones(dias=60, seed=42):
    np.random.seed(seed)
    data = []

    for dia in range(dias):
        if np.random.rand() < 0.15:
            montos = np.random.exponential(scale=4000, size=200)
        else:
            montos = np.random.normal(loc=1200, scale=300, size=200)

        for monto in montos:
            data.append([dia, max(monto, 10)])

    return pd.DataFrame(data, columns=["dia", "monto"])
