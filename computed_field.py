from pydantic import BaseModel,AnyUrl,Field,field_validator,EmailStr,computed_field
from typing import Annotated as Annotation

class Student(BaseModel):
    """Example student model with a computed BMI field."""
    name:str
    age:Annotation[int,Field(default=18,description="This is the age of the student",gt=0,lt=100)]
    wieght:int|None = None
    bio:Annotation[str  | None,Field(default=None,description="This is a bio of the student")]
    hobbies:list[str]|None = None
    link : AnyUrl|None = None
    email: EmailStr


    @field_validator('email')
    @classmethod
    def email_validator(cls,value:EmailStr):
        # This demo only accepts a couple of university-style domains.
        valid_domains = ["edu.com","nu.com"]
        domain = value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError(f"Invalid email domain: {domain}. Allowed domains are: {valid_domains}")   
        return value

    @computed_field
    @property
    def bmi(self)->float:
        return self.wieght/self.age




def readStudent(student:Student):
    print(student.name)
    print(student.age)
    print(student.bio)
    print(student.hobbies)
    print(student.link)
    print(student.email)
    print(student.bmi)


student:Student  =Student(name="Tayyab", age=21,wieght =60,bio="I am a student of computer science", hobbies=["Reading","Coding"], link="https://www.google.com", email="tayyab@nu.com")

readStudent(student)
