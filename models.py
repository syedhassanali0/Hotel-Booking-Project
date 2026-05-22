from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class BookingCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    check_in: date
    check_out: date
    room_type: str
    guests: int
    special_requests: Optional[str] = ""


class BookingOut(BookingCreate):
    id: int
    created_at: str

    class Config:
        from_attributes = True
