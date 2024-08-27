from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from pymongo import MongoClient

app = FastAPI()

templates = Jinja2Templates(directory="templates")


def get_database():
    """Connect to the MongoDB database and return the collection."""
    client = MongoClient("mongodb://mongo/rapidPrototype")
    return client['data_collection']


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    collection = get_database()

    return templates.TemplateResponse("index.html.jinja2", {"request": request})