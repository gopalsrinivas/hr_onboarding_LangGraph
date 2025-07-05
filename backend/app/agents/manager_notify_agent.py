import logging
from app.logger.logger import setup_logger
from app.schemas.state_schema import OnboardingState
from app.crud.employee_crud import update_employee

logger = setup_logger("manager_notify_agent")


def notify_manager(state: OnboardingState) -> OnboardingState:
    try:
        logger.info(f"Notifying manager for employee {state.employee_id}")
        updated_state = state.copy(update={"manager_notified": True})
        # ✅ Correct DB field
        update_employee(
            employee_id=updated_state.employee_id,
            update_data={"manager_notified": updated_state.manager_notified},
        )
        return updated_state
    except Exception as e:
        logger.error(f"Error notifying manager: {e}")
        return state
