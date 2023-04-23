from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from os.path import realpath

def configuration_route(app: FastAPI, no_wind_day_number: int):
    app.mount(
        "/static",
        StaticFiles(directory=realpath(f"{realpath(__file__)}/../static")),
        name="static",
    )
    app.mount(
        "/graphs",
        StaticFiles(directory=realpath(f"{realpath(__file__)}/../graphs")),
        name="graphs",
    )
    templates = Jinja2Templates(directory="application/website/templates")

    @app.get('/')
    def index(request: Request):
        return templates.TemplateResponse("index.html", {"request": request})

    @app.get('/les-dix-annees-les-plus-chaudes-depuis-1996', response_class=HTMLResponse)
    def dix_annee(request: Request):
        return templates.TemplateResponse("dix_annees.html", {"request": request})

    @app.get('/changement-de-temperature-dans-le-temps', response_class=HTMLResponse)
    def changement_temp(request: Request):
        return templates.TemplateResponse("changement_temp.html", {"request": request})

    @app.get('/jour-ou-les-eoliennes-n-ont-pas-tounees', response_class=HTMLResponse)
    def jour_de_vent(request: Request):
        return templates.TemplateResponse("jour_de_vent.html", {"request": request, "no_wind_day_number":no_wind_day_number, 
                                                                "no_wind_month_number": no_wind_day_number/30,
                                                                "no_wind_year_number": no_wind_day_number/365.25})

    @app.get('/fort-changement-de-temperature-dans-une-semaine', response_class=HTMLResponse)
    def fort_changement_dans_semaine(request: Request):
        return templates.TemplateResponse("fort_changement_temp_semaine.html", {"request": request})
    
    return app