import logging
from app.logger.logger import setup_logger
from app.schemas.state_schema import OnboardingState
from app.crud.employee_crud import update_employee

logger = setup_logger("orientation_agent")


def schedule_orientation(state: OnboardingState) -> OnboardingState:
    try:
        logger.info(f"Scheduling orientation for employee {state.employee_id}")
        updated_state = state.copy(update={"orientation_scheduled": True})
        # ✅ Correct DB field
        update_employee(
            employee_id=updated_state.employee_id,
            update_data={"orientation_scheduled": updated_state.orientation_scheduled},
        )
        return updated_state
    except Exception as e:
        logger.error(f"Error scheduling orientation: {e}")
        return state
