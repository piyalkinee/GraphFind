import random
from database.core import database_sql, connect_neo4j, DB_NAME

genSumbols = "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ"


async def create_graph_for_sql(iterations_count: int):

    query: str = ""
    buffer_id: int = None
    vertex_to_create: dict = {"null": [generate_name()]}
    buffer_vertex_to_create: dict = {}

    for iteration in range(iterations_count):
        for vertex_key in vertex_to_create:

            for vertex_value in vertex_to_create[vertex_key]:

                query = f"INSERT INTO `{DB_NAME}`.`vertices` (`name`,`iter`) VALUES ('{vertex_value}','{iteration}');"
                buffer_id = await database_sql.execute(query)

                if vertex_key != "null":
                    query = f"INSERT INTO `{DB_NAME}`.`edges` (`from_id`,`to_id`) VALUES ('{vertex_key}','{buffer_id}');"
                    await database_sql.execute(query)

                buffer_vertex_to_create[buffer_id] = create_new_vertex_list()

        vertex_to_create = buffer_vertex_to_create
        buffer_vertex_to_create = {}


async def create_graph_for_neo4j(formated_graph: dict):
    query: str = "CREATE "

    for vertex in formated_graph:
        query += f'(ver_{vertex}:vertex' + '{name:"' + str(vertex) + '"}),'

    query = query[:-1]

    session = connect_neo4j()

    session.run(query)


def create_new_vertex_list(min_vertices_in_iteration: int = 1, max_vertices_in_iteration: int = 4):
    vertex: list = []

    for new_vertex in range(random.randint(min_vertices_in_iteration, max_vertices_in_iteration)):
        vertex.append(generate_name())

    return vertex


def generate_name():
    name = ""

    for x in range(random.randint(2, 12)):
        name += random.choice(list(genSumbols))

    return name


def generate_age():
    return random.randint(16, 90)
