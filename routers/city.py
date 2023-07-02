from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

import models.models as models
import schemas.schemas as schemas
from database.database import get_db

router = APIRouter()


@router.get("/")
def get_city_data(
    db: Session = Depends(get_db), limit: int = 10, page: int = 1, cod_city: int = -1
):
    skip = (page - 1) * limit

    cond_id = models.CityModel.cod_city == cod_city if cod_city != -1 else True

    data = db.query(models.CityModel).filter(cond_id).limit(limit).offset(skip).all()
    return {"status": "success", "results": len(data), "notes": data}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_data(payload: schemas.CityBaseSchema, db: Session = Depends(get_db)):
    new_data = models.CityModel(**payload.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {"status": "success", "data": new_data}


@router.patch("/{dataId}")
def update_note(
    dataId: int, payload: schemas.CityBaseSchema, db: Session = Depends(get_db)
):
    data_query = db.query(models.CityModel).filter(models.CityModel.cod_city == dataId)
    db_data = data_query.first()

    if not db_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No city with this id: {dataId} found",
        )
    update_data = payload.dict(exclude_unset=True)
    data_query.filter(models.CityModel.cod_city == dataId).update(
        update_data, synchronize_session=False
    )
    db.commit()
    db.refresh(db_data)
    return {"status": "success", "data": db_data}


@router.get("/{dataId}")
def get_post(dataId: int, db: Session = Depends(get_db)):
    data = (
        db.query(models.CityModel).filter(models.CityModel.cod_city == dataId).first()
    )
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No data with this id: {dataId} found",
        )
    return {"status": "success", "data": data}


@router.delete("/{dataId}")
def delete_post(dataId: int, db: Session = Depends(get_db)):
    data_query = db.query(models.CityModel).filter(models.CityModel.cod_city == dataId)
    data = data_query.first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No data with this id: {dataId} found",
        )
    data_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
