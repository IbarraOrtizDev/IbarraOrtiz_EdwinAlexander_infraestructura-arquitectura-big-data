<div style="text-align:center">
<img style="width:300px" src="https://www.iudigital.edu.co/images/11.-IU-DIGITAL.png"/>
</div>

<br/>

<div style="text-align:center">
 <h2>Evidencia de aprendizaje 1. Parte 1 del proyecto integrador - Ingestión de Datos desde un API</h2>
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

El proyecto completo (código fuente, scripts, base de datos y archivos generados) deberá estar alojado en un repositorio en GitHub. En el README del repositorio se deberá incluir la trazabilidad del proceso, indicando:

### Descripción breve de la solución
Este proyecto se encarga de la extracción, almacenamiento y verificación de datos desde un API utilizando Python y SQLite. Los datos se obtienen de un API, se almacenan en una base de datos SQLite y se generan archivos de evidencia en formato Excel y texto.

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
.venv/Scripts/activate
```

4. Instalar dependencias

```sh
python -m pip install --upgrade pip
pip install .
```

5. Crear .env para manejar variables de entorno

Variables recomendadas:

```sh
API_URL = 'https://jsonplaceholder.typicode.com/todos/'
DB_PATH = 'src/static/db/ingestion.db'
SAMPLE_FILE_PATH = 'src/static/xlsx/ingestion.xlsx'
AUDIT_FILE_PATH = 'src/static/auditoria/ingestion.txt'
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