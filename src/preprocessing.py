import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Agregar características de fecha
def add_time_features(df):
    df["DATE"] = pd.to_datetime(df["DATE"])
    df["YEAR"] = df["DATE"].dt.year
    df["MONTH"] = df["DATE"].dt.month
    df["DAY"] = df["DATE"].dt.day
    return df


# Agregar características de temperatura
def add_temperature_features(df):
    df["TEMP_MEAN"] = (df["TMAX"] + df["TMIN"]) / 2
    df["TEMP_RANGE"] = df["TMAX"] - df["TMIN"]
    return df

# Crear columnas binarias para lluvia y nieve
def create_rain_target(df):
    df["RAIN"] = (df["PRCP"] > 0).astype(int)
    return df

def create_snow_target(df):
    df["SNOW_DAY"] = (df["SNOW"] > 0).astype(int)
    return df
