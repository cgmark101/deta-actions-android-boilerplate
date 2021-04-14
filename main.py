from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from deta import Deta
from routers import pokemon_routers

deta = Deta()
db = deta.Base('db_name')

app = FastAPI()

app.include_router(pokemon_routers.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/')
async def hello():
    return {'msg':'todo bien'}

@app.get('/hello')
async def hello(request:Request):
    resultado = next(db.fetch())
    titulo = "Generic Python"
    return templates.TemplateResponse("hello.html", {"request": request, "tittle":titulo, 'resultado':resultado})
