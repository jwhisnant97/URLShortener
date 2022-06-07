# shortener_app/config.py

from functools import lru_cache

from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "https://funky-url-shortener.herokuapp.com/"
    db_url: str = "postgresql://rrchqmezqxhdsh:af9f5ac83c828a1d0b05dbfd8e6950af4e24d3b14b9a2c82e41a372078420ae8@ec2-52-72-99-110.compute-1.amazonaws.com:5432/d352q60ue2guqr"

    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for : {settings.env_name}")
    return settings

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for : {settings.env_name}")
    return settings