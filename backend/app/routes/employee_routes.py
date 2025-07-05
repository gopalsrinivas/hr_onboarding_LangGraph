from fastapi import APIRouter, HTTPException
from app.schemas.employee import EmployeeCreate
from app.services.workflow_service import start_onboarding

router = APIRouter()


@router.post("/onboard")
def onboard_employee(employee: EmployeeCreate):
    try:
        employee_id = start_onboarding(employee.dict())
        return {"message": "Onboarding started", "employee_id": employee_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
