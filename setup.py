from setuptools import setup, find_packages

setup(
    name='infraestructura-arquitectura-big-data',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'pandas',
        'openpyxl',  # Necesario para exportar a Excel
        'sqlite3'    # sqlite3 es parte de la biblioteca estándar de Python, no es necesario instalarlo
    ],
    entry_points={
        'console_scripts': [
            'ingestion=ingestion:main',  # Asumiendo que tienes una función main en ingestion.py
        ],
    },
    include_package_data=True,
    description='Proyecto para la extracción, almacenamiento y verificación de datos desde un API utilizando Python y SQLite',
    author='[Tu Nombre]',
    author_email='[Tu Email]',
    url='https://github.com/[tu_usuario]/[nombre_repositorio]',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)