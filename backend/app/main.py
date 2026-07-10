"""
FastAPI application entry point.

This module is responsible for:
- Creating the FastAPI application instance
- Loading application configuration
- Initializing application lifecycle
- Configuring startup and shutdown behavior

Business logic should not live here.
"""


from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api.api import api_router
from app.core.config import settings
from app.core.logging import configure_logging, get_logger


logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifecycle manager.

    Handles:
    - Startup operations
    - Shutdown operations

    Future integrations:
    - Database connection initialization
    - Redis connection
    - ML model loading
    - External service clients
    """

    # Startup
    configure_logging()

    logger.info(
        "Starting application: %s",
        settings.app_name,
    )

    logger.info(
        "Environment: %s",
        settings.environment,
    )

    yield

    # Shutdown
    logger.info(
        "Shutting down application: %s",
        settings.app_name,
    )


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "Enterprise AI Service Desk Backend API"
    ),
    lifespan=lifespan,
)


# ============================================================
# Future Application Registrations
# ======================================================
app.include_router(api_router)
# Example:
#
# from app.api.api import api_router
# app.include_router(api_router)


# Middleware registration will be added here later.
#
# Example:
#
# app.add_middleware(SomeMiddleware)


# Global exception handlers will be registered here later.
#
# Example:
#
# @app.exception_handler(CustomException)
# async def custom_exception_handler(...):
#     ...