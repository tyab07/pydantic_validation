from pydantic import BaseModel,AnyUrl,Field
from typing import Annotated as Annotation

class Student(BaseModel):
    name:str
    age:Annotation[int,Field(default=18,description="This is the age of the student",gt=0,lt=100)]
    bio:Annotation[str,Field(default=None,description="This is a bio of the student")]
    hobbies:list[str]|None = None
    link : AnyUrl|None = None


def readStudent(student:Student):
    print(student.name)
    print(student.age)
    print(student.bio)
    print(student.hobbies)
    print(student.link)

student:Student  =Student(name="Tayyab", age=21, bio="I am a student of computer science", hobbies=["Reading","Coding"], link="https://www.google.com")

readStudent(student)
