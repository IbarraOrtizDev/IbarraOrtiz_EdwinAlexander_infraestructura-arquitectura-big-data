import pandas as pd
import numpy as np
import random

def crash_data(df):
    df_sucio = df.copy()

    # 1. Agregar valores nulos de manera aleatoria
    for col in df_sucio.columns:
        df_sucio.loc[df_sucio.sample(frac=0.1).index, col] = np.nan

    # 2. Duplicar algunas filas
    df_sucio = pd.concat([df_sucio, df_sucio.sample(frac=0.1)], ignore_index=True)

    # 3. Introducir errores tipográficos en "Customer_Name"
    def typo(text):
        if pd.notna(text) and random.random() < 0.2:
            text = list(text)
            idx = random.randint(0, len(text) - 1)
            text[idx] = random.choice('abcdefghijklmnopqrstuvwxyz')
            return "".join(text)
        return text

    df_sucio["Customer_Name"] = df_sucio["Customer_Name"].apply(typo)

    # 4. Agregar valores atípicos en "Units_Sold" y "Revenue"
    df_sucio.loc[df_sucio.sample(frac=0.05).index, "Units_Sold"] *= 100
    df_sucio.loc[df_sucio.sample(frac=0.05).index, "Revenue"] *= 100

    return df_sucio