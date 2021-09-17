import databases
from neo4j import GraphDatabase
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "mysql://root:1231@localhost:3306/graphfindDB"
NEO4J_DATABASE_URL = "bolt://localhost:7687"

DB_NAME = "graphfinddb"

database_sql = databases.Database(SQLALCHEMY_DATABASE_URL)
neo4j_driver = GraphDatabase.driver(NEO4J_DATABASE_URL, auth=("neo4j", "1231"))

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

metadata = MetaData()


def connect_neo4j():
    return neo4j_driver.session(database="graphdb")
