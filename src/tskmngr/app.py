from fastapi import FastAPI

from . import api

tags_metadata = [
    {
        'name': 'auth',
        'description': 'Authorization and authentication'
    },
    {
        'name': 'tasks',
        'description': 'Create, read, update and delete tasks.'
    }
]

app = FastAPI(
    title='Task Manager',
    description='Simple Task Manager for personal usage',
    version='1.0.0',
    openapi_tags=tags_metadata,
)
app.include_router(api.router)
