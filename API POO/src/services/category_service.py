from sqlalchemy.orm import Session
from src.databases import tables_model
from src.models.category_schema import CategoryCreate, CategoryOut

# Obtener todas las categorías
def get_categories(db: Session):
    return db.query(tables_model.Categoria).all()

# Obtener una categoría por su ID
def get_category(db: Session, categoria_id: int):
    return db.query(tables_model.Categoria).filter(tables_model.Categoria.id == categoria_id).first()

# Crear una nueva categoría
def create_category(db: Session, categoria: CategoryCreate):
    # Use .dict() for Pydantic v1, or .model_dump() for Pydantic v2
    try:
        # Try Pydantic v2 approach first
        categoria_dict = categoria.model_dump()
    except AttributeError:
        # Fall back to Pydantic v1 approach
        categoria_dict = categoria.dict()
        
    db_categoria = tables_model.Categoria(**categoria_dict)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

# Actualizar una categoría
def update_category(db: Session, categoria_id: int, datos: CategoryCreate):
    categoria = get_category(db, categoria_id)
    if categoria:
        # Use .dict() for Pydantic v1, or .model_dump() for Pydantic v2
        try:
            # Try Pydantic v2 approach first
            datos_dict = datos.model_dump()
        except AttributeError:
            # Fall back to Pydantic v1 approach
            datos_dict = datos.dict()
            
        for key, value in datos_dict.items():
            setattr(categoria, key, value)
        db.commit()
        db.refresh(categoria)
    return categoria

# Eliminar una categoría
def delete_category(db: Session, categoria_id: int):
    categoria = get_category(db, categoria_id)
    if categoria:
        db.delete(categoria)
        db.commit()
    return categoria