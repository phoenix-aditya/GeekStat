'''
Module to generate & update codeforces problem set
on the database
'''
import requests
from tqdm import tqdm
from database_driver import (
    return_latest_doc_in_collection,
    check_if_collection_exists,
    insert_documents
)

def generate_or_update_cf_problem_set():
    '''
    function to generate & update the problem set
    on the MongoDB database
    '''
    res = requests.get(
        "https://codeforces.com/api/problemset.problems"
    ).json()

    if res['status'] != "OK":
        return False
    
    res = res['result']['problems']

    # case when the problem set collection does not exist
    if check_if_collection_exists('problemset') is False:
        list_for_database = []

        print('parsing response from codeforces')
        for plbm in tqdm(res):
            temp_obj = {}
            if 'rating' not in plbm:
                continue

            temp_obj['pid'] = str(str(plbm['contestId'])+plbm['index'])
            temp_obj['name'] = plbm['name']
            temp_obj['contestID'] = plbm['contestId']
            temp_obj['index'] = plbm['index']
            temp_obj['rating'] = plbm['rating']
            temp_obj['tags'] = plbm['tags']

            list_for_database.append(temp_obj)
        list_for_database.reverse()

        insert_documents(
            collection_name='problemset',
            list_of_document=list_for_database
        )

    else:
        last_updated_problem = return_latest_doc_in_collection('problemset')
        
        # can have a better binary search implementation here
        index = 0
        for plbm in res:
            if plbm['contestId'] == last_updated_problem['contestID'] and plbm['index'] == last_updated_problem['index']:
                break

            index += 1
        print(index)

        new_problems = []
        for i in range(0, index):
            temp_obj = {}
            plbm = res[i]
            if 'rating' not in plbm:
                continue
            
            temp_obj['pid'] = str(str(plbm['contestId'])+plbm['index'])
            temp_obj['name'] = plbm['name']
            temp_obj['contestID'] = plbm['contestId']
            temp_obj['index'] = plbm['index']
            temp_obj['rating'] = plbm['rating']
            temp_obj['tags'] = plbm['tags']

            new_problems.append(temp_obj)
        
        new_problems.reverse()

        insert_documents(
            collection_name='problemset',
            list_of_document=new_problems
        )

    return True
        

    
