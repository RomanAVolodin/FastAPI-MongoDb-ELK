from pydantic import BaseModel


class Author(BaseModel):
    first_name: str
    last_name: str
