# Importamos los módulos necesarios de SQLAlchemy y dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Cargamos las variables de entorno desde .env
load_dotenv()

# Obtenemos la URL de la base de datos desde la variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Creamos el engine que se conecta a la base de datos
engine = create_engine(DATABASE_URL)

# Creamos una clase para manejar sesiones de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declaramos la base para los modelos ORM 
# (El ORM es una técnica que permite interactuar con una base de datos 
# relacional (como PostgreSQL, MySQL, SQLite, etc.) utilizando 
# código orientado a objetos)
Base = declarative_base()