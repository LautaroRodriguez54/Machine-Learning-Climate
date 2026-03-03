# Predicción de lluvia mediante Machine Learning  
## Proyecto de Data Science – Serie Temporal Climática

---

## Dataset

Este proyecto utiliza datos climáticos históricos provenientes de la estación meteorológica:

**Caribou Weather Forecast Office (USW00014607)**  
Administrada por la **National Oceanic and Atmospheric Administration (NOAA)**  
Dataset: Global Historical Climatology Network – Daily (GHCN-Daily)

Período analizado: 2020 – 2025  
Frecuencia: Datos diarios

Variables utilizadas:

- DATE → Fecha
- TMAX → Temperatura máxima diaria (°C)
- TMIN → Temperatura mínima diaria (°C)
- PRCP → Precipitación diaria (mm)
- SNOW → Nieve caída diaria (mm)
- SNWD → Nieve acumulada en superficie (mm)

---

## Objetivo del Proyecto

Desarrollar un modelo de clasificación supervisada capaz de predecir si un día presentará lluvia (`RAIN = 1`) o no (`RAIN = 0`) utilizando variables meteorológicas observadas.

El problema se aborda como:

> Clasificación binaria en una serie temporal climática.

---

## Hipótesis de Trabajo

### Hipótesis Principal

H1:  
Es posible predecir la ocurrencia de lluvia diaria a partir de variables térmicas y condiciones de superficie (nieve acumulada).

---

### Hipótesis Físicas Subyacentes

1. La temperatura máxima y mínima influyen en la probabilidad de precipitación líquida.
2. La amplitud térmica diaria puede actuar como indicador indirecto de estabilidad atmosférica.
3. La presencia de nieve acumulada puede modificar la probabilidad de precipitación líquida.
4. La lluvia es un fenómeno no puramente aleatorio, sino condicionado por variables atmosféricas medibles.

---

## Metodología Utilizada (Hasta el Momento)

### 1 Obtención de datos

Los datos fueron descargados mediante la API REST oficial de NOAA en formato JSON, lo cual permitió:

- Automatización del proceso
- Reproducibilidad
- Control de variables descargadas

---

### 2 Estructuración del Proyecto

Se implementó una arquitectura modular:

Separación clara entre:
- Exploración (notebooks)
- Lógica reutilizable (src)

---

### 3 Ingeniería de Variables

Se generaron variables derivadas:

- TEMP_MEAN = (TMAX + TMIN) / 2
- TEMP_RANGE = TMAX - TMIN
- YEAR, MONTH, DAY
- Variable objetivo:  
  RAIN = 1 si PRCP > 0

---

### 4 Análisis Exploratorio (EDA)

Se realizó:

- Análisis de proporción de días con lluvia (~43%)
- Análisis de estacionalidad
- Gráficos mensuales de nieve vs temperatura media
- Evaluación de distribución temporal

---

### 5 División Temporal del Dataset

Dado que se trata de una serie temporal, se evitó el uso de `train_test_split` aleatorio.

Se utilizó un corte cronológico:

- Entrenamiento: 2020 – 2024
- Test: 2025

Esto respeta la causalidad temporal y evita data leakage.

---

### 6 Modelo Inicial

Se entrenó un modelo de:

Decision Tree Classifier

Parámetros iniciales:

- max_depth = 4
- min_samples_leaf = 20
- random_state = 42

El objetivo de este modelo inicial es:

- Obtener interpretabilidad
- Analizar variables más relevantes
- Establecer una línea base (baseline)

---

## Próximos Pasos

- Evaluación detallada de métricas (Precision, Recall, F1)
- Comparación con KNN
- Incorporación de variables temporales (rolling mean)
- Análisis de importancia de variables
- Evaluación de overfitting
- Eventual extensión a clasificación multiclase (seco / lluvia / nieve)

---

## Enfoque Científico

Este proyecto combina:

- Fundamentos físicos (termodinámica y procesos atmosféricos)
- Análisis estadístico
- Machine Learning supervisado
- Buenas prácticas de ingeniería de datos

---

## Tecnologías Utilizadas

- Python 3.11
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn
- Conda (gestión de entorno)

---

## Estado Actual

Proyecto en desarrollo – Fase de modelado inicial.

