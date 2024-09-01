from pahina_server.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    date = Column(String)

