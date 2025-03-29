import os
def generateAuditReport(df_sales, df_data_initial):
    file_path = "src/static/auditoria/staticenrichment_report.txt"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, "w") as file:
        file.write("Reporte de Enriquecimiento de Datos\n\n")
        file.write(f"Registros en dataset base: \n")
        file.write(f"{len(df_data_initial)}\n")
        file.write(f"Registros después del enriquecimiento:\n")
        file.write(f"{len(df_sales)}\n")
        file.write(f"Total de columnas en dataset base: {len(df_data_initial.columns)}\n")
        file.write(f"Total de columnas en dataset enriquecido: {len(df_sales.columns)}\n")
        file.write("\n--- Detalles de Integración ---\n")
        file.write(f"Registros coincidentes en 'Customer': {df_sales['CUSTOMER'].notna().sum()}\n")
        file.write(f"Registros coincidentes en 'Product': {df_sales['PRODUCT'].notna().sum()}\n")
        file.write("\n--- Estadísticas de Datos ---\n")
        file.write(f"Total de registros: {len(df_sales)}\n")
        file.write(f"Total de columnas: {len(df_sales.columns)}\n")
        file.write(f"Total de valores nulos: {df_sales.isnull().sum().sum()}\n")
        file.write(f"Valores nulos por columna:\n")
        for col, null_count in df_sales.isnull().sum().items():
            file.write(f"  - {col}: {null_count}\n")
        file.write(f"Total de registros duplicados: {df_sales.duplicated().sum()}\n")
        file.write(f"Valores duplicados por columna:\n")
        for col in df_sales.columns:
            file.write(f"  - {col}: {df_sales[col].duplicated().sum()}\n")
        # List of columns names
        file.write("\n--- Nombres de columnas dataset inicial ---\n")
        file.write(f"{df_data_initial.columns.tolist()}\n")

        # List of columns names
        file.write("\n--- Nombres de columnas dataset enriquecido ---\n")
        file.write(f"{df_sales.columns.tolist()}\n")

        file.write("\n--- Operaciones Realizadas ---\n")
        file.write("1. Eliminación de registros duplicados.\n")
        file.write("2. Eliminación de filas con valores nulos.\n")
        file.write("3. Enriquecimiento de datos con información adicional.\n")
        file.write("4. Conversión de tipos de datos.\n")
        file.write("5. Exportación de datos enriquecidos a CSV.\n")
