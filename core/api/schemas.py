from pydantic import BaseModel
from typing import Any


class Result(BaseModel):
    erro: Any | None = None
    success: Any | None = None
