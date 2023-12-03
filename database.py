from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://pizza:salam1234@localhost:5432/book',
                       echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker()

