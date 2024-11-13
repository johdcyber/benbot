# config.py
import os
from dotenv import dotenv_values

# Load environment variables from config.txt
config = dotenv_values("config.txt")

class Config:
    SECRET_KEY = config.get("SECRET_KEY", "a_random_secret_key")
    DATABASE_URL = config.get("DATABASE_URL", "sqlite:///./test.db")  # Default to SQLite for testing
