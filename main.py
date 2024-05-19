from fastapi import FastAPI, Request
from database.connection import migrate
from fastapi.staticfiles import StaticFiles
from config.initializer import initialize as initialize_config
app = FastAPI()
initialize_config(app)
app.mount("/static", StaticFiles(directory="static"), name="static")

# on startup
@app.on_event("startup")
async def startup_event():
    migrate()

