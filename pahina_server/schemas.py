from pydantic import BaseModel

class ProjectBase(BaseModel):
    title: str
    content: str
    date: str

class ProjectModel(ProjectBase):
    id: int

    class Config:
        orm_mode: True