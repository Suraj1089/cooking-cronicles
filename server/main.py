from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")


templates = Jinja2Templates(directory="frontend")


links = [
    {"label": "Home", "url": "index.html"},
    {"label": "Our Menus", "url": "menu.html"},
    {"label": "Blog Entries", "url": "blog.html"},
    {"label": "Contact Us", "url": "contact.html"},
]


@app.get("/", response_class=HTMLResponse)
async def Home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request, "links": links})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "links": links})

@app.get("/blogs", response_class=HTMLResponse)
async def blogs(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request, "links": links})

@app.get("/menus", response_class=HTMLResponse)
async def menu(request: Request):
    return templates.TemplateResponse("menu.html", {"request": request, "links": links})
