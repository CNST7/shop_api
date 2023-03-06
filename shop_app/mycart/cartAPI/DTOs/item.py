from dataclasses import dataclass
from uuid import UUID


@dataclass()
class ItemDTO:
    external_id: str
    cart: UUID
    name: str | None = None
    value: int | None = None
