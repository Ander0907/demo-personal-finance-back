from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from typing import Optional

class UserCreateIn(BaseModel):
    nombre: str = Field(min_length=1, max_length=120)
    cedula: str = Field(pattern=r"^\d{5,20}$")
    email: str = Field(min_length=5, max_length=255)
    activo: bool = True

class UserOut(BaseModel):
    id: int
    nombre: str
    cedula: str
    email: str
    activo: bool
    created_at: datetime

    # Pydantic v2: permite construir desde la entidad (dataclass)
    model_config = ConfigDict(from_attributes=True)
