from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

# Read data
df_wine= pd.read_csv("Data/wine-clustering.csv")


# Create FastAPI app
app = FastAPI()

# Ruta funcion 1
@app.get('/wine')
async def wine_data():
    df_json = df_wine.to_json(orient="records")
    return JSONResponse(content=df_json, media_type="application/json")
    