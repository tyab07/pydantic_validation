from pydantic import BaseModel


class Address(BaseModel):
    """Simple address model for a patient record."""
    street:str
    city:str
    state:str
    zip_code:str

class Patient(BaseModel):
    name:str
    age:int
    address:Address




def initialize_patient_data()->Patient:
    address = Address(street="123 Main St", city="New York", state="NY", zip_code="10001")
    patient = Patient(name="John Doe", age=30, address=address)
    return patient


def viewPatientData(patient:Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Address: {patient.address.street}, {patient.address.city}, {patient.address.state} {patient.address.zip_code}")

viewPatientData(initialize_patient_data())
