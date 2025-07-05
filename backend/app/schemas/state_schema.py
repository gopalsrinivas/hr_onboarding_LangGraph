from pydantic import BaseModel
from typing import Annotated


class OnboardingState(BaseModel):
    employee_id: Annotated[int, "readonly"]
    documents_verified: bool = False
    it_setup_done: bool = False
    orientation_scheduled: bool = False
    manager_notified: bool = False
    payroll_updated: bool = False
