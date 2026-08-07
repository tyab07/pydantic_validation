from pydantic import BaseModel, AnyUrl, Field, model_validator
from typing import Annotated as Annotation

class Student(BaseModel):
    name: str
    age: Annotated[int, Field(default=18, description="This is the age of the student", gt=0, lt=100)]
    bio: Annotated[str, Field(default=None, description="This is a bio of the student")]
    hobbies: list[str] | None = None
    link: AnyUrl | None = None

    @model_validator(mode="after")
    def age_model(model):
        if model.age < 18 and model.hobbies and "Reading" not in model.hobbies:
            raise ValueError("Age must be greater than or equal to 18 or include Reading")
        return model


def read_student(student: Student):
    print(student.name)
    print(student.age)
    print(student.bio)
    print(student.hobbies)
    print(student.link)


student = Student(
    name="Tayyab",
    age=10,
    bio="I am a student of computer science",
    hobbies=["Reading", "Coding"],
    link="https://www.google.com",
)

read_student(student)
