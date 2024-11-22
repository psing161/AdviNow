from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from typing import Optional, List

from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from service.business_service import *

router = APIRouter()


@router.get('/status')
async def get_status():
    try:
        return {"Health OK"}

    except Exception as e:
        return {'Error: ' + str(e)}


@router.post('/business_symptom')
async def post_business_and_symptom(business_id: Optional[str] = Query(None, description="Filter by business ID"),
                                    diagnostic: bool = None):
    try:
        return query_db_on_business_id_and_diagnostic(business_id, diagnostic)
    except Exception as e:
        return {'Error: ' + str(e)}


@router.post('/upload_csv')
async def upload_file_to_db(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only CSV is allowed.")

    try:
        await save_csv_data_to_db(file)
        return JSONResponse(content={"message": "Data from CSV uploaded successfully"}, status_code=200)

    except pd.errors.ParserError:
        raise HTTPException(status_code=400, detail="Error parsing CSV file.")

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")



