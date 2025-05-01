from sqlalchemy.orm import Session
from src.databases import tables_model
from src.models.supplier_schema import SupplierCreate, SupplierOut

# Obtener todos los proveedores
def get_suppliers(db: Session):
    return db.query(tables_model.Proveedor).all()

# Obtener un proveedor por su ID
def get_supplier(db: Session, proveedor_id: int):
    return db.query(tables_model.Proveedor).filter(tables_model.Proveedor.id == proveedor_id).first()

# Crear un nuevo proveedor
def create_supplier(db: Session, proveedor: SupplierCreate):
    # Use .dict() for Pydantic v1, or .model_dump() for Pydantic v2
    try:
        # Try Pydantic v2 approach first
        proveedor_dict = proveedor.model_dump()
    except AttributeError:
        # Fall back to Pydantic v1 approach
        proveedor_dict = proveedor.dict()
        
    db_proveedor = tables_model.Proveedor(**proveedor_dict)
    db.add(db_proveedor)
    db.commit()
    db.refresh(db_proveedor)
    return db_proveedor

# Actualizar un proveedor
def update_supplier(db: Session, proveedor_id: int, datos: SupplierCreate):
    proveedor = get_supplier(db, proveedor_id)
    if proveedor:
        # Use .dict() for Pydantic v1, or .model_dump() for Pydantic v2
        try:
            # Try Pydantic v2 approach first
            datos_dict = datos.model_dump()
        except AttributeError:
            # Fall back to Pydantic v1 approach
            datos_dict = datos.dict()
            
        for key, value in datos_dict.items():
            setattr(proveedor, key, value)
        db.commit()
        db.refresh(proveedor)
    return proveedor

# Eliminar un proveedor
def delete_supplier(db: Session, proveedor_id: int):
    proveedor = get_supplier(db, proveedor_id)
    if proveedor:
        db.delete(proveedor)
        db.commit()
    return proveedor