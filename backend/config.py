from pydantic_settings import BaseSettings
import os

from typing import Optional

class Settings(BaseSettings):
    # Make fields optional during initialization
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    TEST_DATABASE_URL: Optional[str] = os.getenv("TEST_DATABASE_URL")

    class Config:
        env_file = (
            ".env"
        )
        env_file_encoding = 'utf-8'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.validate()

    def validate(self):
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL must be set")
        if not self.TEST_DATABASE_URL:
            raise ValueError("TEST_DATABASE_URL must be set")

settings = Settings()