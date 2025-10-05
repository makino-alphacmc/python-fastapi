from fastapi import FastAPI
from routers import contact

app = FastAPI()

app.include_router(contact.router)

