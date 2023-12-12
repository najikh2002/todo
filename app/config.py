from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "TODO"
    database_url: str = ""

settings = Settings()