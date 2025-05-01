from pydantic import BaseModel

class SupplierBase(BaseModel):
    nombre_empresa: str
    telefono: str
    correo: str
    direccion: str

class SupplierCreate(SupplierBase):
    pass

class SupplierOut(SupplierBase):
    id: int

    class Config:
        from_attributes = True