from fastapi import FastAPI
from src.apis import product_routes, category_routes, supplier_routes
from src.databases.db import Base, engine

# Creamos todas las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

# Creamos la instancia principal de la aplicación FastAPI
app = FastAPI()

# Incluimos las rutas de libros en la app
app.include_router(product_routes.router)
app.include_router(category_routes.router)
app.include_router(supplier_routes.router)