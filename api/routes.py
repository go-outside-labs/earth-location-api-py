# -*- encoding: utf-8 -*-
# api/routes.py

from pydantic import BaseModel
from fastapi import APIRouter
from .methods import get_location


router = APIRouter()


class City(BaseModel):
    city: str


@router.post("/")
def search_city(data: City) -> dict:

    try:
        return get_location(data.city.lower())

    except KeyError as e:
        return {'error': 'KeyError: {}'.format(e)}
