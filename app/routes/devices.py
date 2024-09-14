from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.Device])
async def get_devices(db: Session = Depends(get_db)):
    return crud.read_devices(db)
