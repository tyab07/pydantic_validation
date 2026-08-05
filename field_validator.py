from pydantic import BaseModel, AnyUrl, Field, EmailStr
from typing import Annotated as Annotation

class Student(BaseModel):
    name: str
    age: Annotation[int, Field(default=18, description="This is the age of the student", gt=0, lt=100)]
    bio: Annotation[str | None, Field(default=None, description="This is a bio of the student")]
    hobbies: list[str] | None = None
    link: AnyUrl | None = None
    email: EmailStr

    @field_validator('email')
    @classmethod
    def email_validator(cls, value: EmailStr) -> EmailStr:
        valid_domains = ["edu.com", "nu.com"]
        domain = value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError(f"Invalid email domain: {domain}. Allowed domains are: {valid_domains}")
        return value


def read_student(student: Student):
    print(student.name)
    print(student.age)
    print(student.bio)
    print(student.hobbies)
    print(student.link)
    print(student.email)


student: Student = Student(
    name="Tayyab",
    age=21,
    bio="I am a student of computer science",
    hobbies=["Reading", "Coding"],
    link="https://www.google.com",
    email="tayyab@nu.com",
)

read_student(student)
