from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.databases.db import SessionLocal
from src.services import supplier_service
from src.models.supplier_schema import SupplierCreate, SupplierOut

# Creamos un router para agrupar las rutas de proveedores
router = APIRouter()

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Cerramos sesión al finalizar

# Ruta para obtener todos los proveedores
@router.get("/proveedores", response_model=list[SupplierOut])
def listar_proveedores(db: Session = Depends(get_db)):
    return supplier_service.get_suppliers(db)

# Ruta para obtener un proveedor por su ID
@router.get("/proveedores/{proveedor_id}", response_model=SupplierOut)
def obtener_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    proveedor = supplier_service.get_supplier(db, proveedor_id)
    if not proveedor:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return proveedor

# Ruta para crear un proveedor nuevo
@router.post("/proveedores", response_model=SupplierOut)
def crear_proveedor(proveedor: SupplierCreate, db: Session = Depends(get_db)):
    return supplier_service.create_supplier(db, proveedor)

# Ruta para actualizar un proveedor existente
@router.put("/proveedores/{proveedor_id}", response_model=SupplierOut)
def actualizar_proveedor(proveedor_id: int, proveedor: SupplierCreate, db: Session = Depends(get_db)):
    return supplier_service.update_supplier(db, proveedor_id, proveedor)

# Ruta para eliminar un proveedor
@router.delete("/proveedores/{proveedor_id}")
def eliminar_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    proveedor = supplier_service.delete_supplier(db, proveedor_id)
    if not proveedor:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return {"mensaje": "Proveedor eliminado correctamente"}