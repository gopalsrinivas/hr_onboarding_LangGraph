import logging
from app.logger.logger import setup_logger
from app.schemas.state_schema import OnboardingState
from app.crud.employee_crud import update_employee

logger = setup_logger("document_agent")


def verify_documents(state: OnboardingState) -> OnboardingState:
    try:
        logger.info(f"Verifying documents for employee {state.employee_id}")
        updated_state = state.copy(update={"documents_verified": True})
        # ✅ Correct DB field
        update_employee(
            employee_id=updated_state.employee_id,
            update_data={"documents_verified": updated_state.documents_verified},
        )
        return updated_state
    except Exception as e:
        logger.error(f"Error verifying documents: {e}")
        return state
