from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

engine = create_engine('sqlite:///tentacle-web.sqlite', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# this method will only run once, when the database is created
def init_db():
    Base.metadata.create_all(bind=engine)
    db_session.commit()

if __name__ == "__main__":
    init_db()