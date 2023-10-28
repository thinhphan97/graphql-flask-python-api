from ariadne import (ObjectType, graphql_sync, load_schema_from_path,
                     make_executable_schema, snake_case_fallback_resolvers)
from ariadne.constants import PLAYGROUND_HTML
from flask import jsonify, request

from api import app, db
from api.mutations import (create_post_resolver, delete_post_resolver,
                           update_post_resolver)
from api.queries import getPost_resolver, listPosts_resolver
from dotenv import load_dotenv

load_dotenv()
mutation = ObjectType("Mutation")
mutation.set_field("createPost", create_post_resolver)
mutation.set_field("updatePost", update_post_resolver)
mutation.set_field("deletePost", delete_post_resolver)

query = ObjectType("Query")
query.set_field("listPosts", listPosts_resolver)
query.set_field("getPost", getPost_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)
type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code