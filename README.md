# 🌧️ Rain Prediction using Machine Learning

Proyecto de Data Science enfocado en la predicción de precipitaciones mediante técnicas de Machine Learning utilizando datos meteorológicos históricos.

## 🎯 Objetivo

Desarrollar un modelo capaz de predecir la ocurrencia de lluvia al día siguiente a partir de variables climáticas observadas, evaluando diferentes algoritmos de clasificación y su capacidad de generalización.

## 📊 Dataset

Datos meteorológicos diarios provenientes de la estación:

**Caribou Weather Forecast Office (USW00014607)**
Fuente: NOAA – Global Historical Climatology Network (GHCN)

Periodo analizado: **2020–2025**

## 🔍 Proceso desarrollado

* Limpieza y preparación de datos
* Análisis Exploratorio (EDA)
* Ingeniería de variables
* Selección de características
* Entrenamiento y comparación de modelos
* Optimización de hiperparámetros
* Validación cruzada estratificada
* Evaluación e interpretación de resultados

## 🤖 Modelos evaluados

* Logistic Regression
* XGBoost
* Support Vector Machine (SVM)

## 🏆 Resultado Final

El modelo **SVM optimizado** obtuvo el mejor desempeño general:

| Métrica   | Valor |
| --------- | ----- |
| Accuracy  | 0.80  |
| Precision | 0.76  |
| Recall    | 0.79  |
| F1 Score  | 0.77  |
| ROC-AUC   | 0.88  |

## 📌 Principales Hallazgos

* Las variables relacionadas con humedad, temperatura, presión atmosférica y viento fueron las más relevantes para la predicción.
* La disponibilidad y calidad de los datos tuvo un impacto mayor que la elección del algoritmo.
* Los modelos de Machine Learning demostraron capacidad para anticipar eventos de precipitación utilizando únicamente información meteorológica histórica.

## 🛠️ Tecnologías

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Matplotlib
* Seaborn

## 📂 Estructura del Proyecto

```text
data/
models/
notebooks/
results/
src/
```

## 🚀 Estado

✅ Proyecto finalizado

Incluye análisis exploratorio, ingeniería de variables, comparación de modelos, optimización de hiperparámetros y conclusiones finales.