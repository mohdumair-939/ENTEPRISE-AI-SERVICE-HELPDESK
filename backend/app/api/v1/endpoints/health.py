"""
Health check endpoint.

Used to verify that the API service is running.
"""


from fastapi import APIRouter

from app.core.config import settings
from pydantic import BaseModel


router = APIRouter()


class HealthResponse(BaseModel):
    """
    Response schema for health endpoint.
    """

    status: str
    service: str
    version: str


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health check",
    description="Returns application health status.",
)
async def health_check() -> HealthResponse:
    """
    Health check endpoint.

    Currently performs only application-level validation.

    Future additions:
    - Database connectivity check
    - Redis availability
    - External service checks
    """

    return HealthResponse(
        status="healthy",
        service="Enterprise AI Service Desk Backend",
        version=settings.app_version,
    )