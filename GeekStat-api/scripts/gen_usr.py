from operator import truediv
import requests
import json
import pickle


def generate_usr_file(usr):
    res = requests.get(
        "https://codeforces.com/api/user.status?handle="+usr).json()
    
    if(res['status']=='FAILED'):
        return False
    
    usr_data = {}
    usr_info = requests.get(
        "https://codeforces.com/api/user.info?handles="+usr).json()
    usr_data['cf_rating'] = usr_info['result'][0]['rating']
    usr_data['cf_max_rating'] = usr_info['result'][0]['maxRating']
    usr_data['cf_handle'] = usr_info['result'][0]['handle']
    usr_data['cf_rank'] = usr_info['result'][0]['rank']

    usr_data['category_count'] = {}
    usr_data['cf_solved_problems'] = []

    for intel in res['result']:
        if intel['verdict'] == 'OK':
            prlbm = intel['problem']
            usr_data['cf_solved_problems'].append(str(prlbm['contestId'])+str(prlbm['index']))
            for tag in prlbm['tags']:
                if tag not in usr_data['category_count']:
                    usr_data['category_count'][tag] = {}
                    if prlbm['index'] not in usr_data['category_count'][tag]:
                        usr_data['category_count'][tag][prlbm['index']] = 1
                    else:
                        usr_data['category_count'][tag][prlbm['index']]+=1
                else:
                    if prlbm['index'] not in usr_data['category_count'][tag]:
                        usr_data['category_count'][tag][prlbm['index']] = 1
                    else:
                        usr_data['category_count'][tag][prlbm['index']]+=1
    
    # adding ratings from other platforms
    cf_rating_graph = [0]
    data = requests.get("https://codeforces.com/api/user.rating?handle="+usr).json()
    for i in data['result']:
        cf_rating_graph.append(i['newRating'])
    
    usr_data['cf_graph'] = cf_rating_graph

    file = open("database/"+usr+".pkl", "wb")
    pickle.dump(usr_data, file)
    file.close()

    file = open("database/"+usr+".pkl", "wb")
    pickle.dump(usr_data, file)
    file.close()
    
    return usr_data

def gen_spoj_data(usr):
    usr_data={}
    # spoj
    data = requests.get("https://competitive-coding-api.herokuapp.com/api/spoj/"+usr).json()
    if data['status'] == 'Success':
        usr_data['spoj'] = 'True'
        usr_data['spoj_handle'] = data['username']
        usr_data['spoj_points'] = data['points']
        usr_data['spoj_rank'] = data['rank']
        usr_data['spoj_problem_solved'] = len(data['solved'])
    else:
        usr_data['spoj'] ='False'
    return usr_data

def gen_atcoder_data(usr):
    # atcoder
    usr_data={}
    data = requests.get("https://competitive-coding-api.herokuapp.com/api/atcoder/"+usr).json()
    if data['status'] == 'Success':
        usr_data['atcoder'] = 'True'
        usr_data['atcoder_handle'] = data['username']
        usr_data['atcoder_rating'] = data['rating']
        usr_data['atcoder_highest'] = data['highest']
        usr_data['atcoder_rank'] = data['rank']
        usr_data['atcoder_level'] = data['level']
    else:
        usr_data['atcoder'] = 'False'
    return usr_data

def gen_leetcode_data(usr):
    usr_data={}
    #leetcode
    data = requests.get("https://competitive-coding-api.herokuapp.com/api/leetcode/"+usr).json()
    if data['message'] == 'Internal Server Error':
        usr_data['leetcode'] = 'False'
        return usr_data
    
    if data['status'] == 'Success':
        usr_data['leetcode'] = 'True'
        usr_data['leetcode_easy_questions_solved'] = data['easy_questions_solved']
        usr_data['leetcode_easy_acceptance_rate'] = data['easy_acceptance_rate']
        usr_data['leetcode_medium_questions_solved'] = data['medium_questions_solved']
        usr_data['leetcode_medium_acceptance_rate'] = data['medium_acceptance_rate']
        usr_data['leetcode_hard_questions_solved'] = data['hard_questions_solved']
        usr_data['leetcode_hard_acceptance_rate'] = data['hard_acceptance_rate']
    
        usr_data['leetcode_total_easy_questions'] = data['total_easy_questions']
        usr_data['leetcode_total_medium_questions'] = data['total_medium_questions']
        usr_data['leetcode_total_hard_questions'] = data['total_hard_questions']
    else:
        usr_data['leetcode'] = 'False'
    return usr_data