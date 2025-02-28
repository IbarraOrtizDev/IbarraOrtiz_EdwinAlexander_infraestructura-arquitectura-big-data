@echo off
python -m venv .venv
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install .
echo API_URL=https://jsonplaceholder.typicode.com/todos/ > .env
echo DB_PATH=src/static/db/ingestion.db >> .env
echo SAMPLE_FILE_PATH=src/static/xlsx/ingestion.xlsx >> .env
echo AUDIT_FILE_PATH=src/static/auditoria/ingestion.txt >> .env
mkdir src\static\db src\static\xlsx src\static\auditoria
python src/ingestion.py