from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class CategoryType(str, Enum):
    INGREDIENT = "INGREDIENTE"
    BEVERAGE = "BEBIDA"
    UTENSIL = "UTENSILIO"
    FURNITURE = "MOBILIARIO"
    CLEANING = "LIMPIEZA"
    OFFICE = "OFICINA"
    PICNIC = "PICNIC"
    DECORATION = "DECORACION"
    UNIFORM = "UNIFORME"

class PerishableType(str, Enum):
    PERISHABLE = "PERECEDERO"
    NON_PERISHABLE = "NO_PERECEDERO"

# Schemas de Categoría
class CategoryBase(BaseModel):
    name: str = Field(..., description="Nombre de la categoría")
    type: CategoryType = Field(..., description="Tipo de categoría")
    description: Optional[str] = Field(None, description="Descripción de la categoría")

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    
    class Config:
        orm_mode = True

# Schemas de Item
class ItemBase(BaseModel):
    name: str = Field(..., description="Nombre del item")
    description: Optional[str] = Field(None, description="Descripción del item")
    category_id: int = Field(..., description="ID de la categoría a la que pertenece")
    perishable_type: Optional[PerishableType] = Field(None, description="Tipo de perecibilidad")
    minimum_stock: Optional[int] = Field(0, description="Stock mínimo requerido")
    unit: Optional[str] = Field(None, description="Unidad de medida")
    price: Optional[float] = Field(None, description="Precio unitario")
    is_active: bool = Field(True, description="Estado activo/inactivo del item")

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    
    class Config:
        orm_mode = True

# Schemas de Proveedor
class SupplierBase(BaseModel):
    name: str = Field(..., description="Nombre del proveedor")
    contact_person: Optional[str] = Field(None, description="Persona de contacto")
    email: Optional[EmailStr] = Field(None, description="Correo electrónico")
    phone: Optional[str] = Field(None, description="Teléfono")
    address: Optional[str] = Field(None, description="Dirección")

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int
    
    class Config:
        orm_mode = True

# Schemas de Item de Proveedor
class SupplierItemBase(BaseModel):
    supplier_id: int = Field(..., description="ID del proveedor")
    item_id: int = Field(..., description="ID del item")
    price: Optional[float] = Field(None, description="Precio del proveedor")
    minimum_order_quantity: Optional[int] = Field(None, description="Cantidad mínima de orden")
    lead_time_days: Optional[int] = Field(None, description="Días de entrega")

class SupplierItemCreate(SupplierItemBase):
    pass

class SupplierItem(SupplierItemBase):
    id: int
    
    class Config:
        orm_mode = True

# Schemas de Movimiento de Inventario
class InventoryMovementBase(BaseModel):
    item_id: int = Field(..., description="ID del item")
    quantity: float = Field(..., description="Cantidad")
    movement_type: str = Field(..., description="Tipo de movimiento (entrada/salida)")
    reference_number: Optional[str] = Field(None, description="Número de referencia")
    notes: Optional[str] = Field(None, description="Notas adicionales")

class InventoryMovementCreate(InventoryMovementBase):
    pass

class InventoryMovement(InventoryMovementBase):
    id: int
    date: datetime
    
    class Config:
        orm_mode = True

# Schemas de Almacenamiento
class StorageBase(BaseModel):
    name: str = Field(..., description="Nombre del almacén")
    type: str = Field(..., description="Tipo de almacén")
    temperature_range: Optional[str] = Field(None, description="Rango de temperatura")
    capacity: float = Field(..., description="Capacidad total")
    current_usage: float = Field(0, description="Uso actual")

class StorageCreate(StorageBase):
    pass

class Storage(StorageBase):
    id: int
    
    class Config:
        orm_mode = True

# Schemas de Conteo de Inventario
class InventoryCountBase(BaseModel):
    item_id: int = Field(..., description="ID del item")
    storage_id: int = Field(..., description="ID del almacén")
    quantity: float = Field(..., description="Cantidad contada")
    counted_by: str = Field(..., description="Responsable del conteo")

class InventoryCountCreate(InventoryCountBase):
    pass

class InventoryCount(InventoryCountBase):
    id: int
    last_count_date: datetime
    
    class Config:
        orm_mode = True