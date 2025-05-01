# product_service.py
from sqlalchemy.orm import Session
from src.databases import tables_model
from src.models.product_schema import ProductoCreate

# Obtener todos los productos
def get_products(db: Session):
    return db.query(tables_model.Producto).all()

# Obtener un producto por su ID
def get_product(db: Session, producto_id: int):
    return db.query(tables_model.Producto).filter(tables_model.Producto.id == producto_id).first()

# Crear un nuevo producto
def create_product(db: Session, producto: ProductoCreate):
    # Use .dict() for Pydantic v1, or .model_dump() for Pydantic v2
    try:
        # Try Pydantic v2 approach first
        producto_dict = producto.model_dump()
    except AttributeError:
        # Fall back to Pydantic v1 approach
        producto_dict = producto.dict()
        
    db_producto = tables_model.Producto(**producto_dict)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# Actualizar un producto
def update_product(db: Session, producto_id: int, datos: ProductoCreate):
    producto = get_product(db, producto_id)
    if producto:
        # Use .dict() for Pydantic v1, or .model_dump() for Pydantic v2
        try:
            # Try Pydantic v2 approach first
            datos_dict = datos.model_dump()
        except AttributeError:
            # Fall back to Pydantic v1 approach
            datos_dict = datos.dict()
            
        for key, value in datos_dict.items():
            setattr(producto, key, value)
        db.commit()
        db.refresh(producto)
    return producto

# Eliminar un producto
def delete_product(db: Session, producto_id: int):
    producto = get_product(db, producto_id)
    if producto:
        db.delete(producto)
        db.commit()
    return producto

# Obtener productos por categoría
def get_products_by_category(db: Session, categoria_id: int):
    return db.query(tables_model.Producto).filter(tables_model.Producto.id_categoria == categoria_id).all()

# Obtener productos por proveedor
def get_products_by_supplier(db: Session, proveedor_id: int):
    return db.query(tables_model.Producto).filter(tables_model.Producto.id_proveedor == proveedor_id).all()