from data_generation import generar_transacciones
from feature_engineering import calcular_kurtosis
from anomaly_detection import detectar_anomalias

def pipeline_produccion():
    df = generar_transacciones()
    df_kurt = calcular_kurtosis(df)
    df_resultado = detectar_anomalias(df_kurt)
    return df, df_resultado

if __name__ == "__main__":
    df_transacciones, df_alertas = pipeline_produccion()
    
    df_alertas.to_csv("alertas.csv", index=False)
    
    print("Archivo alertas.csv generado correctamente")
    print(df_alertas.head())


