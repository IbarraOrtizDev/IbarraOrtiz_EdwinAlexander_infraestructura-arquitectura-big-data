<div style="text-align:center">
<img style="width:300px" src="https://www.iudigital.edu.co/images/11.-IU-DIGITAL.png"/>
</div>

<br/>

<div style="text-align:center">
 <h2>Evidencia de aprendizaje 1. Parte 1 del proyecto integrador - Ingestión de Datos desde un API</h2>
</div>
<div style="text-align:center">
 <h2>S25 - EA2. Preprocesamiento y Limpieza de Datos en Plataforma de Big Data en la Nube</h2>
</div>
<div style="text-align:center">
 <h2>S25 - EA3. Enriquecimiento de Datos en Plataforma de Big Data en la Nube</h2>
</div>
<br/>

## Integrantes
<br/>
<div style="text-align:center">
 <h3>Edwin Alexander Ibarra Ortiz</h3>
 <h3>PREICA2501B010112</h3>
</div>
<br/>
<div style="text-align:center">
 <h3>Sergio Andres Rios Gomez</h3>
 <h3>PREICA2501B010112</h3>
</div>
<br/>
<br/>

<div style="text-align:center">
 <h3>IU Digital de Antioquia</h3>
 <h3>Ingeniería de Software y Datos</h3>
 <h3>2025</h3>
</div>

## Descripción del Proyecto

El proyecto utiliza GitHub Actions para automatizar el proceso de ingestión de datos. El workflow definido en bigdata.yml realiza las siguientes tareas:

1. Clona el repositorio.
2. Genera un entorno virtual y activa el entorno.
3. Instala las dependencias necesarias.
4. Genera un UUID único para identificar los archivos generados.
5. Crea los directorios necesarios para almacenar la base de datos y los archivos de evidencia.
6. Crea un archivo .env con las rutas y configuraciones necesarias.
7. Ejecuta el script de ingestión para extraer datos del API, almacenarlos en la base de datos y generar los archivos de evidencia.
8. Realiza un commit y push de los archivos generados al repositorio.

#### Verificación de la creación de la base de datos y la generación de los archivos de evidencia
Para verificar que la base de datos y los archivos de evidencia se han creado correctamente, puedes revisar los archivos generados en los siguientes directorios:

- Base de datos: db
- Archivo Excel: xlsx
- Archivo de auditoría: auditoria

Estos archivos se generan y actualizan automáticamente cada vez que se ejecuta el workflow de GitHub Actions.

### Instrucciones para clonar el repositorio, instalar dependencias y ejecutar los scripts

1. Clonar el repositorio:
   ```sh
   git clone https://github.com/IbarraOrtizDev/IbarraOrtiz_EdwinAlexander_infraestructura-arquitectura-big-data
   cd infraestructura-arquitectura-big-data
   ```
2. Si tienes windows puedes ejecutar y omitir los pasos siguientes:
```sh
./setup_and_run.bat
```

2. Crear entorno virtual

```sh
python -m venv .venv
```

3. Activar entorno

```sh
.venv/Scripts/activate
```
OR
```BASH
.venv/bin/activate
```

4. Instalar dependencias

```sh
python -m pip install --upgrade pip
pip install .
```

5. Crear .env para manejar variables de entorno

Variables recomendadas:

```sh
API_URL_USUARIOS = 'https://jsonplaceholder.typicode.com/todos/'
API_URL = 'https://www.kaggle.com/api/v1/datasets/download/alejandromontero1/ventas'
DB_PATH = 'src/static/db/ingestion.db'
SAMPLE_FILE_PATH = 'src/static/xlsx/ingestion.xlsx'
AUDIT_FILE_PATH = 'src/static/auditoria/ingestion.txt'
REPORT_FILE_PATH = 'src/static/auditoria/cleaning_report.txt'
REPORT_FILE_PATH_MD = 'src/static/auditoria/cleaning_report_.md'
CLEANED_FILE_PATH = 'src/static/xlsx/cleaning_.csv'
```

6. Crear las carpetas 

/static/db/
/static/xlsx/
/static/auditoria/

```sh
mkdir -p src/static/db src/static/xlsx src/static/auditoria
```

7. Ejecutar el script de ingestión:

```sh
python src/ingestion.py
```

8. Ejecutar el script de limpieza de datos

```sh
python src/cleaning.py
```

9. Ejecutar el script de enriched

```sh
python src/enrichment.py
```

## Conclusiones entrega #2

El proceso de limpieza y preprocesamiento de datos ha sido fundamental para garantizar la calidad y confiabilidad del conjunto de datos de ventas. A continuación, se presentan las conclusiones basadas en los resultados obtenidos:

1. Mejora en la Calidad de los Datos
Eliminación de Valores Nulos: Se eliminaron todas las filas con valores nulos, lo que redujo el conjunto de datos de 5,478 registros a 2,163 registros. Esto asegura que no haya datos faltantes que puedan afectar los análisis posteriores.
Manejo de Outliers: Se identificaron y eliminaron valores atípicos en las columnas Units_Sold y Revenue, lo que contribuye a un análisis más robusto y confiable.
Corrección de Tipos de Datos: Se aseguró que cada columna tenga el tipo de dato correcto, lo que facilita las operaciones de análisis y evita errores en cálculos futuros.

2. Reducción del Tamaño del Conjunto de Datos
El número de registros se redujo de 5,478 a 2,163, lo que indica que se eliminaron aproximadamente 3,315 registros que no cumplían con los criterios de calidad. Esta reducción es significativa y refleja la cantidad de datos inconsistentes o incompletos en el conjunto original.

3. Generación de Evidencias
Archivo de Datos Limpios: Se exportó el conjunto de datos limpio a un archivo CSV (cleaned_data.csv), listo para su uso en las siguientes etapas del proyecto.

Archivo de Auditoría: Se generó un archivo de auditoría (cleaning_report.txt) que documenta todas las operaciones realizadas y compara el estado de los datos antes y después de la limpieza. Esto garantiza la trazabilidad del proceso y permite verificar el impacto de cada operación.

4. Operaciones Realizadas
Las siguientes operaciones fueron clave para lograr la calidad de los datos:
Eliminación de Registros Duplicados: Aunque no se encontraron duplicados en este caso, esta operación es crucial para evitar redundancias.
Eliminación de Filas con Valores Nulos: Se eliminaron todas las filas con valores nulos, lo que mejoró la integridad del conjunto de datos.
Eliminación de Datos Atípicos: Se aplicó el rango intercuartílico (IQR) para identificar y eliminar outliers en las columnas Units_Sold y Revenue.
Conversión de Tipos de Datos: Se corrigieron los tipos de datos para asegurar que cada columna tenga el formato adecuado.
Exportación de Datos Limpios: Los datos limpios se guardaron en un archivo CSV para su uso posterior.

5. Impacto del Proceso de Limpieza
Antes de la Limpieza:
Total de registros: 5,478
Valores nulos: 558 en Year, 548 en Month, 548 en Customer, 545 en Product, 548 en Units_Sold, 556 en Price_per_Unit, 554 en Revenue, 549 en Customer_Name, y 548 en Month_Num.

Después de la Limpieza:
Total de registros: 2,163
Valores nulos: 0 en todas las columnas.
Este proceso asegura que los datos estén completos, consistentes y listos para su análisis.

6. Preparación para Análisis Posteriores
Con los datos limpios y estructurados, el conjunto de datos está listo para ser utilizado en etapas posteriores del proyecto, como:

Análisis exploratorio de datos (EDA).
Modelado predictivo.
Generación de informes y visualizaciones.

## Conclusiones entrega #3

Conclusiones
1. Mejora en la Calidad de los Datos
El proceso de enriquecimiento permitió integrar información adicional de múltiples fuentes y formatos (JSON, XLSX, CSV, XML, HTML, TXT), lo que aumentó la profundidad y relevancia del dataset. Esto facilita análisis más precisos y detallados.

2. Consistencia y Normalización
Se aplicaron técnicas de transformación y limpieza para garantizar que los datos fueran consistentes. Esto incluyó la estandarización de nombres de columnas, la conversión de tipos de datos y la eliminación de redundancias.

3. Registro de Auditoría
Se generó un archivo de auditoría (enrichment_report.txt) que documenta las operaciones realizadas, como la cantidad de registros coincidentes, las transformaciones aplicadas y posibles discrepancias detectadas en la integración.

5. Impacto en el Modelado de Datos
El dataset enriquecido proporciona información más completa para la siguiente fase del proyecto (Actividad 4), mejorando la calidad de los insumos utilizados en la construcción de modelos analíticos o de machine learning.

6. Optimización del Almacenamiento
Se definió una estructura de datos eficiente en SQLite, optimizando la organización de la información y facilitando futuras consultas mediante estrategias de almacenamiento separada simulando particiones.