# Importamos los tipos de columnas y relaciones
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.databases.db import Base

# Definimos el modelo de la tabla 'categorias'
class Categoria(Base):
    __tablename__ = "categorias"  # Nombre de la tabla en la BD
    
    # Columnas básicas (igual estructura que el ejemplo Libros)
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    descripcion = Column(String(255))
    
    # Relación con Productos (opcional)
    productos = relationship("Producto", back_populates="categoria")

# Definimos el modelo de la tabla 'proveedores'
class Proveedor(Base):
    __tablename__ = "proveedores"  # Nombre de la tabla en la BD
    
    # Columnas básicas
    id = Column(Integer, primary_key=True, index=True)
    nombre_empresa = Column(String(100))
    telefono = Column(String(20))
    correo = Column(String(100))
    direccion = Column(String(255))
    

    productos = relationship("Producto", back_populates="proveedor")

# Definimos el modelo de la tabla 'productos'
class Producto(Base):
    __tablename__ = "productos"  # Nombre de la tabla en la BD
    
    # Columnas básicas
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    descripcion = Column(String(255))
    precio = Column(Float)
    stock = Column(Integer)
    
    # Claves foráneas (igual que id_categoria en Libros)
    id_categoria = Column(Integer, ForeignKey('categorias.id'))
    id_proveedor = Column(Integer, ForeignKey('proveedores.id'))
    
    # Relaciones (opcionales)
    categoria = relationship("Categoria", back_populates="productos")
    proveedor = relationship("Proveedor", back_populates="productos")