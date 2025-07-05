from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from app.core.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    documents_verified = Column(Boolean, default=False)
    it_setup_done = Column(Boolean, default=False)
    orientation_scheduled = Column(Boolean, default=False)
    manager_notified = Column(Boolean, default=False)
    payroll_updated = Column(Boolean, default=False)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), onupdate=func.now())
