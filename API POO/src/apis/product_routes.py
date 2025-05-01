from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.databases.db import SessionLocal
from src.services import product_service
from src.models.product_schema import ProductoCreate, ProductoOut  # Nombres corregidos

# Creamos un router para agrupar las rutas de productos
router = APIRouter()

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Cerramos sesión al finalizar

# Ruta para obtener todos los productos
@router.get("/productos", response_model=list[ProductoOut])  # Corregido a ProductoOut
def listar_productos(db: Session = Depends(get_db)):
    return product_service.get_products(db)


# Ruta para obtener un producto por su ID
@router.get("/productos/{producto_id}", response_model=ProductoOut)  # Corregido a ProductoOut
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = product_service.get_product(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

# Ruta para crear un producto nuevo
@router.post("/productos", response_model=ProductoOut)  # Corregido a ProductoOut
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):  # Corregido a ProductoCreate
    return product_service.create_product(db, producto)

# Ruta para actualizar un producto existente
@router.put("/productos/{producto_id}", response_model=ProductoOut)  # Corregido a ProductoOut
def actualizar_producto(producto_id: int, producto: ProductoCreate, db: Session = Depends(get_db)):  # Corregido a ProductoCreate
    return product_service.update_product(db, producto_id, producto)

# Ruta para eliminar un producto
@router.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = product_service.delete_product(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado correctamente"}

# Ruta para obtener productos por categoría
@router.get("/categorias/{categoria_id}/productos", response_model=list[ProductoOut])
def listar_productos_por_categoria(categoria_id: int, db: Session = Depends(get_db)):
    productos = product_service.get_products_by_category(db, categoria_id)
    if not productos:
        # No lanzamos excepción, simplemente devolvemos lista vacía
        return []
    return productos

# Ruta para obtener productos por proveedor
@router.get("/proveedores/{proveedor_id}/productos", response_model=list[ProductoOut])
def listar_productos_por_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    productos = product_service.get_products_by_supplier(db, proveedor_id)
    if not productos:
        # No lanzamos excepción, simplemente devolvemos lista vacía
        return []
    return productos