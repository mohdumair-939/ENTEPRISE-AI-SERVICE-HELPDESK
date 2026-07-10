"""
Version 1 API router.

All version 1 endpoints are registered here.
"""


from fastapi import APIRouter

from app.api.v1.endpoints import health


router = APIRouter()


router.include_router(
    health.router,
    tags=["Health"],
)