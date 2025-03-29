
# Reporte de Limpieza de Datos

## Estadísticas Iniciales
- **Total de registros:** 5478
- **Registros duplicados:** 0
- **Valores nulos por columna:**
  - **id:** 0
  - **Year:** 541
  - **Month:** 544
  - **Customer:** 546
  - **Product:** 557
  - **Units_Sold:** 549
  - **Price_per_Unit:** 548
  - **Revenue:** 558
  - **Customer_Name:** 542
  - **Month_Num:** 544

## Estadísticas Finales
- **Total de registros:** {final_stats['total_rows']}
- **Registros duplicados:** {final_stats['total_duplicates']}
- **Valores nulos por columna:**
  - **id:** 0
  - **Year:** 0
  - **Month:** 0
  - **Customer:** 0
  - **Product:** 0
  - **Units_Sold:** 0
  - **Price_per_Unit:** 0
  - **Revenue:** 0
  - **Customer_Name:** 0
  - **Month_Num:** 0

## Operaciones Realizadas
1. Eliminación de registros duplicados.
2. Eliminación de filas con valores nulos.
3. Eliminación de datos atípicos.
4. Conversión de tipos de datos.
5. Exportación de datos limpios a CSV.
