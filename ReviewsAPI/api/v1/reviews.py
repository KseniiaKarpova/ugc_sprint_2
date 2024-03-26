import logging
from uuid import UUID

from fastapi import APIRouter, status, HTTPException
from fastapi_pagination.ext.beanie import paginate
from schemas.review import MarkFilmDto

router = APIRouter(prefix='/reviews', tags=['Comments'])

logger = logging.getLogger().getChild('reviews-router')


@router.post('', status_code=status.HTTP_201_CREATED)
async def mark_film(dto: MarkFilmDto) -> MarkFilmDto:
    pass
