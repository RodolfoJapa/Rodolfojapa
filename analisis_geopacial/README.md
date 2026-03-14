# 🏭 Proyecto de Ciencia de Datos – Sistema de Monitoreo Predictivo y Prescriptivo de Fallas Industriales

## 📌 Descripción del Proyecto
Este proyecto demuestra técnicas de **analítica predictiva, monitoreo de datos en tiempo real y mantenimiento basado en datos** utilizando Python como parte de un **portafolio profesional de Ciencia de Datos**.

El análisis se basa en el dataset **AI4I 2020 Predictive Maintenance Dataset**, que contiene variables operativas de maquinaria industrial como **temperatura, velocidad rotacional, torque y desgaste de herramienta**.

El objetivo del proyecto es **predecir fallas en maquinaria industrial y generar recomendaciones de mantenimiento**, utilizando técnicas de **Machine Learning, detección de anomalías y visualización interactiva**.

El sistema desarrollado simula un **entorno de monitoreo industrial en tiempo real**, donde múltiples máquinas envían datos de sensores que son analizados para detectar riesgos operativos.

El flujo de trabajo del proyecto incluye:

- Ingesta de datos  
- Limpieza y preprocesamiento  
- Análisis exploratorio de datos (EDA)  
- Entrenamiento de modelos de Machine Learning  
- Detección de anomalías  
- Monitoreo de sensores en tiempo real  
- Visualización de métricas operativas en un dashboard  

---

## 🛠️ Tecnologías Utilizadas

- **Python 3**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit**
- **Matplotlib**

**Modelos utilizados:**

- **Random Forest** → Predicción de fallas  
- **Isolation Forest** → Detección de anomalías  

---

## 🗂️ Estructura del Proyecto

---

## 🔄 Flujo de Análisis de Datos

### 1. Carga de datos
Importación del dataset **AI4I Predictive Maintenance**, que contiene información sobre el comportamiento operativo de maquinaria industrial.

Variables principales del dataset:

- Air temperature  
- Process temperature  
- Rotational speed  
- Torque  
- Tool wear  

---

### 2. Limpieza de datos
Se realizó la validación de valores y revisión de tipos de datos para asegurar la consistencia del dataset.

También se verificó el balance de clases en la variable **Machine Failure**.

---

### 3. Análisis Exploratorio de Datos (EDA)

Se analizaron las relaciones entre variables operativas y fallas de máquina, incluyendo:

- Distribución de temperaturas
- Relación entre torque y fallas
- Impacto del desgaste de herramienta
- Identificación de patrones operativos

---

### 4. Modelo de Machine Learning

Se entrenó un modelo de **Random Forest** para predecir la probabilidad de falla de una máquina utilizando variables de sensores.

Variables utilizadas por el modelo:

- Air temperature  
- Process temperature  
- Rotational speed  
- Torque  
- Tool wear  

El modelo estima la **probabilidad de falla de la máquina** en función de sus condiciones operativas.

---

### 5. Detección de anomalías

Se implementó un modelo **Isolation Forest** para detectar comportamientos operativos fuera de lo normal.

Esto permite identificar:

- Condiciones anormales de operación  
- Posibles fallas futuras  
- Patrones inusuales en sensores  

---

### 6. Monitoreo en tiempo real

El sistema simula un flujo continuo de **datos de sensores industriales**, representando múltiples máquinas que envían información periódicamente.

Esto permite observar:

- Cambios en las condiciones operativas  
- Incremento en el riesgo de falla  
- Detección de eventos críticos  

---

### 7. Dashboard interactivo

Se desarrolló un **dashboard interactivo en Streamlit** para visualizar el estado del sistema.

El panel muestra:

- Probabilidad de falla de cada máquina  
- Estimación de vida útil restante (RUL)  
- Alertas operativas  
- Panel de causas de falla (TWF, HDF, PWF, OSF)  
- Detección de anomalías en sensores  

---

## 📈 Visualizaciones Incluidas

El proyecto incluye visualizaciones que permiten interpretar el comportamiento operativo de las máquinas:

- Monitoreo del estado de múltiples máquinas  
- Probabilidad de falla en tiempo real  
- Panel de causas de fallas  
- Detección de anomalías  
- Gráficos de evolución de métricas operativas  

Estas visualizaciones permiten identificar **condiciones de riesgo y anticipar necesidades de mantenimiento**.

---

## 📦 Resultados

El sistema desarrollado permite:

- Predecir fallas en maquinaria industrial  
- Detectar anomalías en condiciones operativas  
- Simular un entorno de monitoreo industrial en tiempo real  
- Visualizar métricas operativas mediante un dashboard interactivo  
- Generar recomendaciones para mantenimiento preventivo  

---

## 👨‍💻 Autor

**Rodolfo Japa**  
Proyecto de Portafolio – Analítica y Ciencia de Datos
