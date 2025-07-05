from app.models.employee import Employee
from app.core.database import SessionLocal
from app.logger.logger import setup_logger
from sqlalchemy.orm.exc import NoResultFound

logger = setup_logger("crud")


def create_employee(employee_data: dict):
    db = SessionLocal()
    try:
        # Check if email already exists
        existing_employee = (
            db.query(Employee).filter_by(email=employee_data["email"]).first()
        )
        if existing_employee:
            logger.info(f"Employee with email {employee_data['email']} already exists.")
            return existing_employee.id  # Return existing employee ID

        # Otherwise, create new employee
        employee = Employee(**employee_data)
        db.add(employee)
        db.commit()
        db.refresh(employee)
        logger.info(f"Created new employee with ID {employee.id}")
        return employee.id
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating employee: {e}")
        raise
    finally:
        db.close()


def get_employee(employee_id: int):
    db = SessionLocal()
    try:
        return db.query(Employee).filter(Employee.id == employee_id).first()
    finally:
        db.close()


def update_employee(employee_id: int, update_data: dict):
    db = SessionLocal()
    try:
        emp = db.query(Employee).get(employee_id)
        if not emp:
            return None
        for key, value in update_data.items():
            setattr(emp, key, value)
        db.commit()
        db.refresh(emp)
        logger.info(f"Updated employee: {emp.id}")
        return emp
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to update employee: {e}")
        raise
    finally:
        db.close()


def delete_employee(employee_id: int):
    db = SessionLocal()
    try:
        emp = db.query(Employee).get(employee_id)
        if not emp:
            return False
        db.delete(emp)
        db.commit()
        logger.info(f"Deleted employee: {employee_id}")
        return True
    finally:
        db.close()
