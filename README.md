# Taller 3: Ingesta, Análisis y Automatización con MongoDB y Python

Proyecto desarrollado para la gestión, almacenamiento y análisis de datos de cervecerías utilizando la API pública **Open Brewery DB** y una base de datos local en **MongoDB**.

## Contenido del Repositorio
- `ingesta.py`: Script en Python encargado de consumir la API de Open Brewery DB, validar registros y almacenarlos en MongoDB sin duplicados.
- `analisis.ipynb`: Notebook de Jupyter que contiene el Análisis Exploratorio de Datos (EDA), los 5 insights estadísticos y las 3 visualizaciones requeridas.
- `requirements.txt`: Archivo con las librerías necesarias para ejecutar el proyecto (`requests`, `pymongo`, `pandas`, `matplotlib`).
- `.gitignore`: Archivo para excluir entornos virtuales y archivos temporales del control de versiones.

## API Utilizada
- **Open Brewery DB**: [https://api.openbrewerydb.org/v1/breweries](https://api.openbrewerydb.org/v1/breweries)

## Cómo Ejecutar el Proyecto
1. Instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
2. Asegurar que el servidor local de MongoDB esté activo.
3. Ejecutar el script de ingesta de datos:
   ```bash
   python ingesta.py
