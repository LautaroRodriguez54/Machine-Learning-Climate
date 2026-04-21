# 🌧️ Predicción de lluvia mediante Machine Learning  
## Proyecto de Data Science – Serie Temporal Climática

---

## 📊 Dataset

Este proyecto utiliza datos climáticos históricos provenientes de la estación meteorológica:

**Caribou Weather Forecast Office (USW00014607)**  
Administrada por la **National Oceanic and Atmospheric Administration (NOAA)**  
Dataset: Global Historical Climatology Network – Daily (GHCN-Daily)

- Período analizado: **2020 – 2025**
- Frecuencia: **Datos diarios**

### Variables originales

- `DATE` → Fecha  
- `TMAX` → Temperatura máxima (°C)  
- `TMIN` → Temperatura mínima (°C)  
- `PRCP` → Precipitación (mm)  
- `SNOW` → Nieve caída (mm)  
- `SNWD` → Nieve acumulada (mm)

---

## 🎯 Objetivo del Proyecto

Desarrollar un modelo de **clasificación supervisada** capaz de predecir si un día presentará lluvia:

- `RAIN = 1` → Hay lluvia  
- `RAIN = 0` → No hay lluvia  

> Problema: Clasificación binaria sobre serie temporal climática.

---

## 🧠 Hipótesis de Trabajo

- La temperatura influye en la probabilidad de precipitación  
- La amplitud térmica refleja estabilidad atmosférica  
- La nieve acumulada impacta en la ocurrencia de lluvia  
- La lluvia no es aleatoria, sino parcialmente predecible mediante variables observables  

---

## ⚙️ Metodología

### 1. Obtención de datos
- Descarga mediante API REST de NOAA  
- Proceso reproducible y automatizado  

---

### 2. Ingeniería de variables

Se generaron nuevas features:

- `TEMP_MEAN = (TMAX + TMIN) / 2`  
- `TEMP_RANGE = TMAX - TMIN`  
- Variables temporales: `YEAR`, `MONTH`, `DAY`  
- Variable objetivo:  
  - `RAIN = 1 si PRCP > 0`

---

### 3. Análisis Exploratorio (EDA)

Se analizaron:

- Distribución de días con lluvia (~43%)  
- Estacionalidad  
- Relación entre temperatura, nieve y precipitación  
- Correlaciones entre variables  

---

### 4. División del dataset

Se utilizó un **split temporal** para evitar data leakage:

- Train → 2020–2024  
- Test → 2025  

---

### 5. Selección de variables

Se aplicó `SelectKBest` con `f_classif` para identificar las variables más relevantes.

Features seleccionadas:

- `TMIN`  
- `TEMP_RANGE`  
- `SNOW`  

---

### 6. Modelado

Se entrenaron y compararon tres modelos de clasificación:

- 🌳 Decision Tree  
- 📈 Logistic Regression  
- 📍 K-Nearest Neighbors (KNN)  

Se aplicó **estandarización de variables** para mantener consistencia y facilitar futuros pipelines.

---

### 7. Evaluación de modelos

Métricas utilizadas:

- Accuracy  
- Matriz de confusión  
- Precision, Recall, F1-score  

#### Resultados principales

| Modelo               | Accuracy |
|---------------------|----------|
| Logistic Regression | ~0.70    |
| KNN                 | ~0.66    |
| Decision Tree       | ~0.66    |

---

## 🏆 Conclusiones

- **Logistic Regression** fue el modelo con mejor desempeño general  
- Los modelos presentan dificultad para detectar correctamente días con lluvia (clase positiva)  
- La simplicidad y estabilidad del modelo lineal lo hacen adecuado para este problema  
- El problema presenta complejidad inherente debido a la naturaleza climática  

---

## 🔄 Pipelines

Se implementaron pipelines con `sklearn.pipeline` para:

- Unificar preprocesamiento y modelado  
- Reducir duplicación de código  
- Facilitar escalabilidad futura  


---

## 🛠️ Tecnologías utilizadas

- Python 3.11  
- Pandas  
- NumPy  
- Matplotlib / Seaborn  
- Scikit-learn  
- Conda  

---

## 🚀 Próximos pasos

- Optimización de hiperparámetros  
- Evaluación con validación cruzada  
- Feature engineering avanzado (rolling features)  
- Incorporación de modelos más complejos (Random Forest, Gradient Boosting)  
- Extensión a problemas multiclase  

---

## 📌 Estado del proyecto

✔ EDA completo  
✔ Feature engineering  
✔ Modelado y comparación de modelos  
✔ Implementación de pipelines  

➡ Proyecto listo para evolución a etapas más avanzadas (DS2 / DS3)