from pydantic import BaseModel
from typing import Optional

class DoProps(BaseModel):
    title: str
    desc: Optional[str] = None
    checklist: bool = False
