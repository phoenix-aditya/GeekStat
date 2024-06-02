'''
The module has a function called is solved
that returns a list of true/false denoting that
if the user has solved the questions recommended to them
'''
from database_driver import return_doc_by_username
from user_service import generate_and_update_user_details
from recommendation_service import recommend_q_to_user
from models import User, Problem

def solved_status(
    username: str
    ):
    '''
    the function returns a list of true/false that denote
    whether a user has solved the recommended questions stored on database 
    yet
    '''
    
    # updating the user details and questions solved
    if generate_and_update_user_details(username=username) == False:
        return None
    
    user = User(return_doc_by_username(
        collection_name='users',
        username=username
    ))

    if len(user.recommended_questions) == 0:
        recommend_q_to_user(username=user.username)

        user = User(return_doc_by_username(
        collection_name='users',
        username=username
        ))
    
    status = []

    for prlbm in user.recommended_questions:
        problem = Problem(prlbm)
        if problem.pid in user.cf_solved_questions_id:
            status.append(True)
        else:
            status.append(False)
    
    return status


