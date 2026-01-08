def detectar_anomalias(df_kurtosis, umbral=3):
    df_kurtosis["anomalia"] = df_kurtosis["kurtosis"] > umbral
    return df_kurtosis
