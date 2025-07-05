import logging
from app.logger.logger import setup_logger
from app.schemas.state_schema import OnboardingState
from app.crud.employee_crud import update_employee

logger = setup_logger("payroll_agent")


def update_payroll(state: OnboardingState) -> OnboardingState:
    try:
        logger.info(f"Updating payroll for employee {state.employee_id}")
        updated_state = state.copy(update={"payroll_updated": True})
        # ✅ Correct DB field
        update_employee(
            employee_id=updated_state.employee_id,
            update_data={"payroll_updated": updated_state.payroll_updated},
        )
        return updated_state
    except Exception as e:
        logger.error(f"Error updating payroll: {e}")
        return state
