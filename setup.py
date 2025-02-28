from setuptools import setup, find_packages

setup(
    name='infraestructura-arquitectura-big-data',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'pandas',
        'openpyxl'
    ],
    entry_points={
        'console_scripts': [
            'ingestion=ingestion:main',
        ],
    },
    include_package_data=True,
    description='Proyecto para la extracción, almacenamiento y verificación de datos desde un API utilizando Python y SQLite',
    author='Edwin Alexander Ibarra - Sergio Rios',
    author_email='edwin.ibarra@est.iudigital.edu.co - sergio.rios@est.iudigital.edu.co',
    url='https://github.com/IbarraOrtizDev/infraestructura-arquitectura-big-data/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)