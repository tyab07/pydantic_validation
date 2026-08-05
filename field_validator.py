from pydantic import BaseModel, AnyUrl, Field, EmailStr
from typing import Annotated as Annotation

class Student(BaseModel):
    name: str
    age: Annotation[int, Field(default=18, description="This is the age of the student", gt=0, lt=100)]
    bio: Annotation[str | None, Field(default=None, description="This is a bio of the student")]
    hobbies: list[str] | None = None
    link: AnyUrl | None = None
