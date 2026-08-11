from fastapi import APIRouter
from app.schemas.patient import PatientCreate, PatientResponse

router = APIRouter(prefix="/api/v1")

_patients: list[dict] = []
_next_id = 1

@router.get("/patients", response_model=list[PatientResponse])
def list_patients():
    return _patients

@router.post("/patients", response_model=PatientResponse, status_code=201)
def create_patient(payload: PatientCreate):
    global _next_id
    patient = {"id": _next_id, **payload.model_dump()}
    _next_id += 1
    _patients.append(patient)
    return patient

@router.get("/command-center")
def command_center():
    return {
        "system": "NovaHIS",
        "status": "operational",
        "modules": ["patients", "command-center", "security"],
    }
