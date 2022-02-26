from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from starlette.responses import FileResponse
import json
import pickle
import sys

from scripts.gen_usr import *
from scripts.recommend_q import *

sys.path.append('final_apis')
app = FastAPI()

# landing page
@app.get("/")
def index():
    return FileResponse("landing/index.html")

@app.get("/genuser/{usr}")
def gen(usr : str):
    status = generate_usr_file(usr)
    if status == 0:
        return {'status':'FAILED'}
    else:
        return {'status': 'OK', 'data': status}

@app.get("/recommendq/{usr}")
def recommend_ques(usr : str):
    recommended = recommend_q(usr)
    if recommended == []:
        return {"status":"FAIL"}
    else:
        ret_data = {"status":"OK", "questions":recommended}
        return ret_data

# use command pip list --format=freeze > requirements.txt
# fast api location: http://127.0.0.1:8000/docs
