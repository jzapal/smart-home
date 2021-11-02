import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from api import schema
from settings import settings, connect_mongodb

graphql_app = GraphQLRouter(schema)

app = FastAPI(title='Smart Home')
app.include_router(graphql_app, prefix="/graphql")


@app.on_event('startup')
def on_startup() -> None:
    connect_mongodb()


if __name__ == '__main__':
    uvicorn.run('api_main:app', host='0.0.0.0',
                port=settings.API_PORT,
                reload=True)
