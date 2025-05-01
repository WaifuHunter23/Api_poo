from pydantic import BaseModel

class CategoryBase(BaseModel):
    nombre: str
    descripcion: str

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int

    class Config:
        from_attributes = True