from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class MemoryInDB(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    user_id: str
    content: str

    class Config:
        populate_by_name = True
