
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.databases.db import SessionLocal
from src.services import category_service
from src.models.category_schema import CategoryCreate, CategoryOut

# Creamos un router para agrupar las rutas de categorías
router = APIRouter()

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Cerramos sesión al finalizar

# Ruta para obtener todas las categorías
@router.get("/categorias", response_model=list[CategoryOut])
def listar_categorias(db: Session = Depends(get_db)):
    return category_service.get_categories(db)

# Ruta para obtener una categoría por su ID
@router.get("/categorias/{categoria_id}", response_model=CategoryOut)
def obtener_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = category_service.get_category(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

# Ruta para crear una categoría nueva
@router.post("/categorias", response_model=CategoryOut)
def crear_categoria(categoria: CategoryCreate, db: Session = Depends(get_db)):
    return category_service.create_category(db, categoria)

# Ruta para actualizar una categoría existente
@router.put("/categorias/{categoria_id}", response_model=CategoryOut)
def actualizar_categoria(categoria_id: int, categoria: CategoryCreate, db: Session = Depends(get_db)):
    return category_service.update_category(db, categoria_id, categoria)

# Ruta para eliminar una categoría
@router.delete("/categorias/{categoria_id}")
def eliminar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = category_service.delete_category(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return {"mensaje": "Categoría eliminada correctamente"}