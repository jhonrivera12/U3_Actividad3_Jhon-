import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from faker import Faker

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

def main():
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(DATABASE_URL)
    metadata = MetaData()
    
    tabla_personas = Table(
        "personas_jhon",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("nombre", String(100)),
        Column("correo", String(150)),
        Column("fecha_nacimiento", Date),
        Column("ciudad", String(100)),
        Column("telefono", String(50)),
        Column("ocupacion", String(100)),
        Column("empresa", String(100))
    )
    
    metadata.create_all(engine)
    print("¡Tabla 'personas_jhon' creada con éxito!")

    fake = Faker('es_ES')
    print("Generando 100.000 registros... Por favor espera un momento.")
    
    registros = []
    for _ in range(100000):
        registros.append({
            "nombre": fake.name(),
            "correo": fake.email(),
            "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=80),
            "ciudad": fake.city(),
            "telefono": fake.phone_number(),
            "ocupacion": fake.job(),
            "empresa": fake.company()
        })

    print("Insertando registros en la base de datos...")
    with engine.begin() as conn:
        chunk_size = 5000
        for i in range(0, len(registros), chunk_size):
            conn.execute(tabla_personas.insert(), registros[i:i + chunk_size])
            
    print("¡100.000 registros insertados correctamente!")

if __name__ == "__main__":
    main()