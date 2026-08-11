from pydantic import BaseModel, Field

class PatientCreate(BaseModel):
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    date_of_birth: str
    national_id: str | None = Field(default=None, max_length=50)

class PatientResponse(PatientCreate):
    id: int
