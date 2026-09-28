import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./fallback_local_factory.db")

# Automatically switch to pg8000 dialect wrapper if connecting to Supabase/Neon
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+pg8000://")

if "sqlite" not in DATABASE_URL:
    engine = create_engine(
        DATABASE_URL, 
        pool_size=3,              # Kept low to stay within limits on Free Tiers
        max_overflow=5,
        pool_pre_ping=True
    )
else:
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_cloud_db_tables():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS agency_clients (
                id SERIAL PRIMARY KEY,
                company_name VARCHAR(255) NOT NULL,
                industry VARCHAR(255) NOT NULL,
                target_audience TEXT NOT NULL,
                tier VARCHAR(50) NOT NULL
            );
        """))
        conn.commit()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
