from fastapi import FastAPI, Request ,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse, JSONResponse
from emp_dao import EmpDao
from pydantic import BaseModel
from typing import Optional
#from emp_dao import EmpDao

app = FastAPI()
ed = EmpDao()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Emp(BaseModel):
    e_id:str = None
    e_name:str= None
    sex:str= None
    addr:str = None

@app.get("/emp", response_class=HTMLResponse)
async def selects(request: Request):
    return templates.TemplateResponse("emp.html", {"request": request})

@app.get("/emp_selects")
async def emp_selects():
    rows = ed.selects()
    return JSONResponse({
        'rows': rows
    })
    
@app.post("/emp_select")
async def emp_select(emp:Emp):
    emp = ed.select(emp.e_id)
    return JSONResponse(emp)
@app.post("/emp_insert")
async def emp_insert(emp:Emp):
    cnt = ed.insert(emp.e_id, emp.e_name, emp.sex, emp.addr)
    return JSONResponse(cnt)

@app.post("/emp_update")
async def emp_update(emp:Emp):
    cnt = ed.update(emp.e_id, emp.e_name, emp.sex, emp.addr)
    return JSONResponse(cnt)
@app.post("/emp_delete")
async def emp_delete(emp:Emp):
    cnt = ed.delete(emp.e_id)
    return JSONResponse(cnt)
#uvicorn myajax:app --reload