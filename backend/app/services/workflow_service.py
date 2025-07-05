from langgraph.graph import StateGraph
from app.agents.document_agent import verify_documents
from app.agents.it_setup_agent import setup_it_access
from app.agents.orientation_agent import schedule_orientation
from app.agents.manager_notify_agent import notify_manager
from app.agents.payroll_agent import update_payroll
from app.crud.employee_crud import create_employee
from app.logger.logger import setup_logger
from app.schemas.state_schema import OnboardingState

logger = setup_logger("workflow")


def start_onboarding(employee_data: dict):
    """
    Orchestrates HR onboarding using LangGraph multi-agent workflow
    """
    employee_id = create_employee(employee_data)

    # Create a state graph
    graph = StateGraph(state_schema=OnboardingState)

    # Add nodes
    graph.add_node("verify_documents", verify_documents)
    graph.add_node("setup_it_access", setup_it_access)
    graph.add_node("schedule_orientation", schedule_orientation)
    graph.add_node("notify_manager", notify_manager)
    graph.add_node("update_payroll", update_payroll)

    # Connect nodes sequentially to avoid conflicts
    graph.add_edge("verify_documents", "setup_it_access")
    graph.add_edge("setup_it_access", "schedule_orientation")
    graph.add_edge("schedule_orientation", "notify_manager")
    graph.add_edge("notify_manager", "update_payroll")

    # Set entry point
    graph.set_entry_point("verify_documents")

    # Compile and run the workflow
    runnable = graph.compile()
    runnable.invoke(OnboardingState(employee_id=employee_id))

    logger.info(f"Workflow completed for employee {employee_id}")
    return employee_id
