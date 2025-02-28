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