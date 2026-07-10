"""
Centralized application logging configuration.

This module provides a single logging configuration point
for the entire application.

Future extensions:
- JSON structured logging
- File handlers
- Cloud logging integrations
- OpenTelemetry integration
"""

import logging
import sys

from app.core.config import settings


LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)


def configure_logging() -> None:
    """
    Configure application-wide logging.

    This function should be called once during application startup.

    Responsibilities:
    - Set global log level.
    - Configure log formatting.
    - Attach console handler.
    """

    log_level = getattr(
        logging,
        settings.log_level.upper(),
        logging.INFO,
    )

    formatter = logging.Formatter(
        LOG_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    root_logger = logging.getLogger()

    root_logger.setLevel(log_level)

    # Prevent duplicate handlers during reloads
    if not root_logger.handlers:
        root_logger.addHandler(console_handler)


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger instance.

    Usage:

        logger = get_logger(__name__)
        logger.info("Application started")

    Args:
        name:
            Usually __name__ of the calling module.

    Returns:
        logging.Logger instance.
    """

    return logging.getLogger(name)