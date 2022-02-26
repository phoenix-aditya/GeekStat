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

    file = open("database/"+usr+".pkl", "wb")
    pickle.dump(usr_data, file)
    file.close()
    
    return True

if __name__=="__main__":
    generate_usr_file("adi_13")
