'''
Main file of the GeekStat backend
the file hosts all the API's for the project
'''
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from database_driver import return_doc_by_username
from user_service import generate_and_update_user_details
from recommendation_service import recommend_q_to_user
from problem_service import generate_or_update_cf_problem_set
from commander import solved_status

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
    return RedirectResponse("/docs")

@app.get("/generate_or_update_user_details/{usr}")
def generate_or_update_user(usr : str):
    '''
    The API generates or updates the user details
    on the database and returns an object of data class
    User
    '''
    status = generate_and_update_user_details(usr)
    if status == False:
        return {'status':'FAILED'}
    else:
        user = return_doc_by_username(
            collection_name='users',
            username=usr
        )
        return {'status': 'OK', 'data':user}

@app.get("/update_recommended_questions/{usr}")
def update_recommended_questions(usr : str):
    '''
    The API updates/refreshes the 10 recommended questions
    that were recommended to the user
    '''
    recommended = recommend_q_to_user(usr)
    if recommended == None:
        return {"status":"FAILED"}
    else:
        return {"status":"OK", "data":recommended}

@app.get("/recommended_question_solve_status/{usr}")
def recommended_question_solve_status(usr : str):
    '''
    the API returns a list of TRUE/FALSE of length 10
    that denotes whether the user has solved the recommended questions
    currently being displayed or not
    '''
    status = solved_status(usr)

    if status == None:
        return {"status":"FAILED"}
    
    return {"status":"OK", "data":status}

@app.get("/update_cf_problemset")
def update_cf_problem_set():
    '''
    The API is to be run using Kaffiene and not by front-end
    to update the cf problem set atleast once a day
    '''
    status = generate_or_update_cf_problem_set()
    
    if status == False:
        return {"status":"FAILED"}
    return {"status":"OK"}

# use command pip list --format=freeze > requirements.txt
# fast api location: http://127.0.0.1:8000/docs
