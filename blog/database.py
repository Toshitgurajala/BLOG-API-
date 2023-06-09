from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

sqldatabseurl =  'sqlite:///./blog.db'

engine = create_engine(sqldatabseurl,connect_args={"check_same_thread":False})

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False )

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()