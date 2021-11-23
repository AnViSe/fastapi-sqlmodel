from sqlmodel import SQLModel, Field


class PersonBase(SQLModel):
    last_name: str
    first_name: str
    middle_name: str


class Person(PersonBase, table=True):
    id: int = Field(default=None, primary_key=True)


class PersonCreate(PersonBase):
    pass
