from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.sqltypes import INTEGER
from database.core import Base, database


class VertexDB(Base):
    __tablename__ = "vertices"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(256))
    iter = Column(Integer)


CourseDBAsync = VertexDB.__table__


class EdgeDB(Base):
    __tablename__ = "edges"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    from_id = Column(String(256))
    to_id = Column(String(256))


CourseDBAsync = VertexDB.__table__
