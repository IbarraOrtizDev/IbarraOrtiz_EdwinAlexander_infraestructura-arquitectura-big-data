@echo off
python -m venv .venv
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install .
echo UUID= >> .env
echo API_URL_USUARIOS=https://jsonplaceholder.typicode.com/todos >> .env
echo API_URL=https://www.kaggle.com/api/v1/datasets/download/alejandromontero1/ventas >> .env
echo DB_PATH=src/static/db/ingestion.db >> .env
echo SAMPLE_FILE_PATH=src/static/xlsx/ingestion.xlsx >> .env
echo AUDIT_FILE_PATH=src/static/auditoria/ingestion.txt >> .env
echo REPORT_FILE_PATH=src/static/auditoria/cleaning_report.txt >> .env
echo REPORT_FILE_PATH_MD=src/static/auditoria/cleaning_report.md >> .env
echo CLEANED_FILE_PATH=src/static/xlsx/cleaning.csv >> .env

mkdir src\static\db src\static\xlsx src\static\auditoria
python src/ingestion.py
python src/cleaning.py
python src/enrichment.py