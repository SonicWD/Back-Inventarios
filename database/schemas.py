from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class TipoCategoria(str, Enum):
    INGREDIENTE = "INGREDIENTE"
    BEBIDA = "BEBIDA"
    UTENSILIO = "UTENSILIO"
    MOBILIARIO = "MOBILIARIO"
    LIMPIEZA = "LIMPIEZA"
    OFICINA = "OFICINA"
    PICNIC = "PICNIC"
    DECORACION = "DECORACION"
    UNIFORME = "UNIFORME"

class TipoPerecedero(str, Enum):
    PERECEDERO = "PERECEDERO"
    NO_PERECEDERO = "NO_PERECEDERO"

# Esquemas de Categoría
class CategoriaBase(BaseModel):
    nombre: str = Field(..., description="Nombre de la categoría")
    tipo: TipoCategoria = Field(..., description="Tipo de categoría")
    descripcion: Optional[str] = Field(None, description="Descripción de la categoría")

class CrearCategoria(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int
    
    class Config:
        from_attributes = True

# Esquemas de Item
class ItemBase(BaseModel):
    nombre: str = Field(..., description="Nombre del item")
    descripcion: Optional[str] = Field(None, description="Descripción del item")
    categoria_id: int = Field(..., description="ID de la categoría a la que pertenece")
    tipo_perecible: Optional[TipoPerecedero] = Field(None, description="Tipo de perecibilidad")
    stock_minimo: Optional[int] = Field(0, description="Stock mínimo requerido")
    unidad: Optional[str] = Field(None, description="Unidad de medida")
    precio: Optional[float] = Field(None, description="Precio unitario")
    activo: bool = Field(True, description="Estado activo/inactivo del item")

class CrearItem(ItemBase):
    pass

class Item(ItemBase):
    id: int
    
    class Config:
        from_attributes = True

# Esquemas de Proveedor
class ProveedorBase(BaseModel):
    nombre: str = Field(..., description="Nombre del proveedor")
    persona_contacto: Optional[str] = Field(None, description="Persona de contacto")
    correo: Optional[EmailStr] = Field(None, description="Correo electrónico")
    telefono: Optional[str] = Field(None, description="Teléfono")
    direccion: Optional[str] = Field(None, description="Dirección")

class CrearProveedor(ProveedorBase):
    pass

class Proveedor(ProveedorBase):
    id: int
    
    class Config:
        from_attributes = True

# Esquemas de Item de Proveedor
class ItemProveedorBase(BaseModel):
    proveedor_id: int = Field(..., description="ID del proveedor")
    item_id: int = Field(..., description="ID del item")
    precio: Optional[float] = Field(None, description="Precio del proveedor")
    cantidad_minima_orden: Optional[int] = Field(None, description="Cantidad mínima de orden")
    tiempo_entrega_dias: Optional[int] = Field(None, description="Días de entrega")

class CrearItemProveedor(ItemProveedorBase):
    pass

class ItemProveedor(ItemProveedorBase):
    id: int
    
    class Config:
        from_attributes = True

# Esquemas de Movimiento de Inventario
class MovimientoInventarioBase(BaseModel):
    item_id: int = Field(..., description="ID del item")
    cantidad: float = Field(..., description="Cantidad")
    tipo_movimiento: str = Field(..., description="Tipo de movimiento (entrada/salida)")
    numero_referencia: Optional[str] = Field(None, description="Número de referencia")
    notas: Optional[str] = Field(None, description="Notas adicionales")

class CrearMovimientoInventario(MovimientoInventarioBase):
    pass

class MovimientoInventario(MovimientoInventarioBase):
    id: int
    fecha: datetime
    
    class Config:
        from_attributes = True

# Esquemas de Almacenamiento
class AlmacenBase(BaseModel):
    nombre: str = Field(..., description="Nombre del almacén")
    tipo: str = Field(..., description="Tipo de almacén")
    rango_temperatura: Optional[str] = Field(None, description="Rango de temperatura")
    capacidad: float = Field(..., description="Capacidad total")
    uso_actual: float = Field(0, description="Uso actual")

class CrearAlmacen(AlmacenBase):
    pass

class Almacen(AlmacenBase):
    id: int
    
    class Config:
        from_attributes = True

# Esquemas de Conteo de Inventario
class ConteoInventarioBase(BaseModel):
    item_id: int = Field(..., description="ID del item")
    almacen_id: int = Field(..., description="ID del almacén")
    cantidad: float = Field(..., description="Cantidad contada")
    responsable: str = Field(..., description="Responsable del conteo")

class CrearConteoInventario(ConteoInventarioBase):
    pass

class ConteoInventario(ConteoInventarioBase):
    id: int
    fecha_ultimo_conteo: datetime
    
    class Config:
        from_attributes = True
