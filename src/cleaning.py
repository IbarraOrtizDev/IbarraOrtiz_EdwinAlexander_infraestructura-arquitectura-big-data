from utils.manageDB import ManageDB
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

db = ManageDB()
df = db.fetch_all_ventas()
# df_ventas = pd.read_json(ventas)
print("READ VENTAS")
print(df.head())
# ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']
month_dic = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

df['Month_Num'] = df['Month'].map(month_dic)

print("DESCRIBE VENTAS")
print("DATOS ESTADISTICOS INICIALES DE VENTAS")
describe = df.describe()
print(describe)

initial_stats = {
    "total_rows": len(df),
    "total_columns": len(df.columns),
    "total_missing": df.isnull().sum().sum(),
    "missing_per_column": df.isnull().sum(),
    "total_duplicates": df.duplicated().sum(),
}


print("ESTADISTICAS INICIALES DE VENTAS")
print(initial_stats)

print("LIMPIEZA DE DATOS")
df_clean = df.copy()
# Drop duplicates
df_clean.drop_duplicates(inplace=True)

# Drop missing values
df_clean.dropna(inplace=True)

# Drop outliers
for col in ["Units_Sold", "Revenue"]:
    Q1 = df_clean[col].quantile(0.25)
    Q3 = df_clean[col].quantile(0.75)
    IQR = Q3 - Q1
    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 * IQR
    df_clean = df_clean[(df_clean[col] >= lim_inf) & (df_clean[col] <= lim_sup)]


print("DESCRIBE VENTAS LIMPIAS")
print("DATOS ESTADISTICOS FINALES DE VENTAS")
describe = df_clean.describe()
print(describe)

final_stats = {
    "total_rows": len(df_clean),
    "total_columns": len(df_clean.columns),
    "total_missing": df_clean.isnull().sum().sum(),
    "missing_per_column": df_clean.isnull().sum(),
    "total_duplicates": df_clean.duplicated().sum(),
}

print("ESTADISTICAS FINALES DE VENTAS")
print(final_stats)

df_clean['Year'] = df_clean['Year'].astype(int)
df_clean['Month'] = df_clean['Month'].astype(str)
df_clean['Units_Sold'] = df_clean['Units_Sold'].astype(int)
df_clean['Price_per_Unit'] = df_clean['Price_per_Unit'].astype(float)
df_clean['Revenue'] = df_clean['Revenue'].astype(float)

print("GUARDANDO DATOS LIMPIOS")
os.getenv('CLEANED_FILE_PATH')
df_clean.to_csv(os.getenv('CLEANED_FILE_PATH'), index=False)


with open(os.getenv('REPORT_FILE_PATH'), 'w') as f:
    f.write("=== Estadisticas Iniciales ===\n")
    f.write(f"Total de registros: {initial_stats['total_rows']}\n")
    f.write(f"Registros duplicados: {initial_stats['total_duplicates']}\n")
    f.write("Valores nulos por columna:\n")
    for col, null_count in initial_stats['missing_per_column'].items():  # Cambiado aquí
        f.write(f"{col}: {null_count}\n")
    
    f.write("\n=== Estadísticas Finales ===\n")
    f.write(f"Total de registros: {final_stats['total_rows']}\n")
    f.write(f"Registros duplicados: {final_stats['total_duplicates']}\n")
    f.write("Valores nulos por columna:\n")
    for col, null_count in final_stats['missing_per_column'].items():  # Cambiado aquí
        f.write(f"{col}: {null_count}\n")
    
    f.write("\n=== Operaciones Realizadas ===\n")
    f.write("1. Eliminacion de registros duplicados.\n")
    f.write("2. Eliminacion de filas con valores nulos.\n")
    f.write("3. Eliminacion de datos atipicos.\n")
    f.write("4. Conversion de tipos de datos.\n")
    f.write("5. Exportacion de datos limpios a CSV.\n")



# Generar informe en Markdown
md_report = f"""
# Reporte de Limpieza de Datos

## Estadísticas Iniciales
- **Total de registros:** {initial_stats['total_rows']}
- **Registros duplicados:** {initial_stats['total_duplicates']}
- **Valores nulos por columna:**
"""

for col, null_count in initial_stats['missing_per_column'].items():
    md_report += f"  - **{col}:** {null_count}\n"

md_report += """
## Estadísticas Finales
- **Total de registros:** {final_stats['total_rows']}
- **Registros duplicados:** {final_stats['total_duplicates']}
- **Valores nulos por columna:**
"""

for col, null_count in final_stats['missing_per_column'].items():
    md_report += f"  - **{col}:** {null_count}\n"

md_report += """
## Operaciones Realizadas
1. Eliminación de registros duplicados.
2. Eliminación de filas con valores nulos.
3. Eliminación de datos atípicos.
4. Conversión de tipos de datos.
5. Exportación de datos limpios a CSV.
"""

# Guardar en un archivo Markdown
with open(os.getenv('REPORT_FILE_PATH_MD'), 'w', encoding='utf-8') as f:
    f.write(md_report)

print("Informe de limpieza guardado en Markdown.")