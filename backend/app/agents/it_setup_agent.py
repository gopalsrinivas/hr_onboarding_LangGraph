import logging
from app.logger.logger import setup_logger
from app.schemas.state_schema import OnboardingState
from app.crud.employee_crud import update_employee

logger = setup_logger("it_setup_agent")


def setup_it_access(state: OnboardingState) -> OnboardingState:
    try:
        logger.info(f"Setting up IT access for employee {state.employee_id}")
        updated_state = state.copy(update={"it_setup_done": True})
        # ✅ Correct DB field
        update_employee(
            employee_id=updated_state.employee_id,
            update_data={"it_setup_done": updated_state.it_setup_done},
        )
        return updated_state
    except Exception as e:
        logger.error(f"Error setting up IT access: {e}")
        return state
