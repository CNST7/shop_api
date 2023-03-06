from pydantic import BaseModel, Field


class Item(BaseModel):
    class Config:
        validate_assignment = True

    id: int | None = None
    external_id: str
    name: str | None = None
    value: int | None = Field(None, title="Price in cents", gt=0)

    def __hash__(self):
        return hash(self.external_id)
