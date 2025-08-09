import os
from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL no está definida")

engine = create_engine(DATABASE_URL, echo=False)