import graphene
import graphql_jwt
import censos.schema

class Query(censos.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

