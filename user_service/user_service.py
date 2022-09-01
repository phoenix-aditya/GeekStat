'''
Main module of user_service package
has all the functions required to generate and update codeforces user data
'''
import requests
from models import User
from database_driver import (
    return_doc_by_username, 
    insert_document,
    update_document_by_username
    )


def update_basic_info(user: User):
    '''
    function to update basic user info from codeforces
    '''
    usr_info = requests.get(
        "https://codeforces.com/api/user.info?handles="+user.username
        ).json()

    if usr_info['status'] == 'FAILED':
        return False
    
    #updating basic information of user
    user.cf_rating = usr_info['result'][0]['rating']
    user.cf_max_rating = usr_info['result'][0]['maxRating']
    user.cf_rank = usr_info['result'][0]['rank']


def update_submission_info(user: User):
    '''
    function to generate and update regarding user submissions
    '''
    database_user_doc = return_doc_by_username(
        collection_name="users", 
        username = user.username
        )
    
    # user data from codeforces API
    usr_submission_status = requests.get(
        "https://codeforces.com/api/user.status?handle="+user.username
        ).json()
    
    if usr_submission_status['status'] == 'FAILED':
        return False
    
    last_logged_problem = "None"

    if database_user_doc != None:
        database_user_doc = User(database_user_doc)
        len_of_solved_q = len(database_user_doc.cf_solved_questions_id)
        if len_of_solved_q>0:
            last_logged_problem = database_user_doc.cf_solved_questions_id[len_of_solved_q-1]

        user.cf_category_count = database_user_doc.cf_category_count
        user.cf_solved_questions_id = database_user_doc.cf_solved_questions_id
    
    temp = []

    for intel in usr_submission_status['result']:
        if intel['verdict'] == 'OK':
            prlbm = intel['problem']
            pid = str(str(prlbm['contestId'])+prlbm['index'])

            if pid == last_logged_problem:
                break
            
            if 'rating' not in prlbm:
                continue

            temp.append(pid)

            for tag in prlbm['tags']:
                if tag not in user.cf_category_count:
                    user.cf_category_count[tag] = {}
                    if prlbm['index'] not in user.cf_category_count[tag]:
                        user.cf_category_count[tag][prlbm['index']] = []
                        user.cf_category_count[tag][prlbm['index']].append(prlbm['rating'])
                    else:
                        user.cf_category_count[tag][prlbm['index']].append(prlbm['rating'])
                else:
                    if prlbm['index'] not in user.cf_category_count[tag]:
                        user.cf_category_count[tag][prlbm['index']] = []
                        user.cf_category_count[tag][prlbm['index']].append(prlbm['rating'])
                    else:
                        user.cf_category_count[tag][prlbm['index']].append(prlbm['rating'])
    
    temp.reverse()
    user.cf_solved_questions_id.extend(temp)

def update_user_rating_changes(user: User):
    '''
    function to update the rating changes for the user
    '''
    user.cf_rating_changes.append(0)

    rating_changes = requests.get(
        "https://codeforces.com/api/user.rating?handle="+user.username
    ).json()
    for i in rating_changes['result']:
        user.cf_rating_changes.append(i['newRating'])


def generate_and_update_user_details(username :str):
    '''
    function to generate and update user details of the
    provided username on the MongoDB database
    '''
    user: User = User()
    user.username = username

    # updating basic information of user
    if update_basic_info(user) == False:
        return False

    #updating user submissions details 
    update_submission_info(user)

    #updating user rating list for graph
    update_user_rating_changes(user)

    database_user_doc = return_doc_by_username(
        collection_name="users", 
        username = user.username
        )

    if database_user_doc == None:
        insert_document(
            collection_name='users',
            document=user.to_primitive()
        )

    else:
        update_document_by_username(
            collection_name='users',
            username=user.username,
            document=user.to_primitive()
        )

    return True



    
    
    
