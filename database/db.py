from sqlmodel import create_engine

DATABASE_URL = 'sqlite:///database/books.db'

engine = create_engine(DATABASE_URL, echo=True)
