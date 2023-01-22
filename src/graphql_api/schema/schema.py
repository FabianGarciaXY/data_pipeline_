import os
from ariadne import make_executable_schema, load_schema_from_path, snake_case_fallback_resolvers
from graphql_api.schema.resolvers.vehicles_resolver import query, error


# Getting the schema
type_defs = load_schema_from_path("{}/src/graphql_api/schema/".format(os.getcwd()))

# Creating the executable schema
schema = make_executable_schema(
    type_defs, [query, error], snake_case_fallback_resolvers
)