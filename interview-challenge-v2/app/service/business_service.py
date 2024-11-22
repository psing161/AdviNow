from app.models import Business, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from settings import DB_URL
import pandas as pd
from fastapi import  Query
from typing import Optional, List


def save_csv_data_to_db(data: pd.DataFrame):
    data['Symptom Diagnostic'] = data['Symptom Diagnostic'].str.lower().map(
        {'true': True, 'yes': True, 'false': False, 'no': False})
    session = create_session()
    symptoms_data = []
    for _, bd in data.iterrows():
        symptoms_data.append(Business(business_id=bd["Business ID"], business_name=bd["Business Name"],
                                      symptom_code=bd["Symptom Code"], symptom_name=bd["Symptom Name"],
                                      symptom_diagnostic=bd["Symptom Diagnostic"]))

    session.add_all(symptoms_data)
    session.commit()

    # Close the session
    session.close()


def query_db_on_business_id_and_diagnostic(business_id, diagnostic: bool):
    session = create_session()
    query = session.query(Business)

    if business_id:
        query = query.filter(Business.business_id == int(business_id))

    if diagnostic is not None:
        query = query.filter(Business.symptom_diagnostic == bool(diagnostic))

    results = query.all()
    result_data = [
        {
            "Business ID": record.business_id,
            "Business Name": record.business_name,
            "Symptom Code": record.symptom_code,
            "Symptom Name": record.symptom_name,
            "Symptom Diagnostic": record.symptom_diagnostic
        }
        for record in results
    ]
    session.close()
    return  result_data


def create_session():
    # Create an engine and a session factory
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
