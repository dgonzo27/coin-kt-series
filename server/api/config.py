"""API configuration"""

import logging
from functools import lru_cache

from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


API_VERSION: str = "0.0.1"
API_TITLE: str = "COIN KT FastAPI"
API_DESCRIPTION: str = "FastAPI for COIN's knowledge transfer sessions."

logger = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    """Base settings for specifying application parameters."""

    api_version: str = f"v{API_VERSION}"
    api_title: str = API_TITLE
    api_description: str = API_DESCRIPTION

    # Postgres connection settings
    database_url: AnyUrl = Field(env="DATABASE_URL", default=None)

    model_config = SettingsConfigDict(extra="allow")


@lru_cache
def get_settings() -> Settings:
    """Get settings helper function."""
    logger.info("loading application config from the current environment.")
    return Settings()
