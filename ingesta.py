import requests
from pymongo import MongoClient

def main():
    # Conexión a MongoDB local
    client = MongoClient("mongodb://localhost:27017/")
    db = client["taller3_db"]
    collection = db["raw_data"]
    
    # Limpiar colección previa para evitar duplicados
    collection.delete_many({})
    
    # Consumir la API de Open Brewery DB (traemos 150 registros para cumplir con los >= 100)
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=150"
    print("Consumiendo datos de la API de Open Brewery DB...")
    
    response = requests.get(url)
    
    if response.status_code == 200:
        breweries = response.json()
        if breweries:
            # Insertar los datos en MongoDB
            collection.insert_many(breweries)
            print(f"¡Éxito! Se insertaron {len(breweries)} documentos en MongoDB (taller3_db.raw_data).")
        else:
            print("La API no devolvió registros.")
    else:
        print(f"Error al conectar con la API: {response.status_code}")

if __name__ == "__main__":
    main()