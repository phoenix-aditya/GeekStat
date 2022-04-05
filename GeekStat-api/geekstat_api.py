from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from starlette.responses import FileResponse
import json
import pickle
import sys

from scripts.gen_usr import *
from scripts.recommend_q import *

from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/leetcode/{usr}")
def leetcode_data(usr: str):
    rec = gen_leetcode_data(usr)

    if rec['leetcode'] == 'False':
        return {"status":"Fail"}
    else:
        return {"status":"OK","data":rec}

@app.get("/spoj/{usr}")
def spoj_data(usr: str):
    rec = gen_spoj_data(usr)

    if rec['spoj'] == 'False':
        return {"status":"Fail"}
    else:
        return {"status":"OK","data":rec}

@app.get("/atcoder/{usr}")
def atcoder_data(usr: str):
    rec = gen_atcoder_data(usr)

    if rec['atcoder'] == 'False':
        return {"status":"Fail"}
    else:
        return {"status":"OK","data":rec}