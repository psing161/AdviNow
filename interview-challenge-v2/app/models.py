from sqlalchemy import Column, Integer, String, DateTime, Boolean,PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
import datetime

Base = declarative_base()


class Business(Base):
    __tablename__ = "business_symptom"

    business_id = Column(Integer)
    business_name = Column(String(100), nullable=False)
    symptom_code = Column(String(100), nullable=False, default="")
    symptom_name = Column(String(100), nullable=False, default="")
    symptom_diagnostic = Column(Boolean, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('business_id', 'symptom_code', name='pk_business_symptom'),
    )
