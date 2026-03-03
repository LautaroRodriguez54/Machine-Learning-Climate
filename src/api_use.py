import requests
import pandas as pd

# -------------------------
# CONFIGURACIÓN
# -------------------------

BASE_URL = "https://www.ncei.noaa.gov/access/services/data/v1"

params = {
    "dataset": "daily-summaries",
    "stations": "USW00014607",  #  CARIBOU WEATHER FORECAST OFFICE, ME US 
    "startDate": "2020-01-01",
    "endDate": "2025-12-31",
    "dataTypes": "DATE,TMAX,TMIN,PRCP,SNOW,AWND",
    "format": "json",
    "units": "metric"
}

# -------------------------
# REQUEST
# -------------------------

response = requests.get(BASE_URL, params=params)

# Verificar que la respuesta sea correcta
if response.status_code == 200:
    data = response.json()
    print("Descarga exitosa ✅")
else:
    print("Error:", response.status_code)
    print(response.text)
    exit()

# -------------------------
# CONVERTIR A DATAFRAME
# -------------------------

df = pd.DataFrame(data)

# Convertir fecha
df["DATE"] = pd.to_datetime(df["DATE"])

# Ordenar por fecha
df = df.sort_values("DATE")

# -------------------------
# GUARDAR ARCHIVO
# -------------------------

df.to_csv("data/raw/ghcn_daily_data.csv", index=False)

print("Archivo guardado como ghcn_daily_data.csv")
print(df.head())
