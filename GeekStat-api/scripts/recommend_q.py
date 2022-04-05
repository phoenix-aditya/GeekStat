import pickle
from scripts.gen_usr import generate_usr_file
from random import sample, shuffle

def get_avg_level(level_solved):
    problems = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    
    sum = 0
    for i in problems:
        if i not in level_solved:
            level_solved[i] = 0
        sum += level_solved[i]
    
    calc = 0
    calc += level_solved['A']*800+level_solved['B']*1000+level_solved['C']*1200
    calc += level_solved['D']*1500 + level_solved['E']*1700+level_solved['F']*2000
    calc += level_solved['G']*2200 + level_solved['H']*2400
    
    return calc/sum+100

def suggested_q_level(avg_lvl):
    if avg_lvl<800: return 'A'
    if avg_lvl<1000: return 'B'
    if avg_lvl<1200: return 'C'
    if avg_lvl<1500: return 'D'
    if avg_lvl<1700: return 'E'
    if avg_lvl<2000: return 'F'
    if avg_lvl<2200: return 'G'
    else: return 'H'


def recommend_q(usr):
    if generate_usr_file(usr) == False:
        return []

    read_file = open("database/"+usr+".pkl", "rb")
    usr_data = pickle.load(read_file)
    
    problems = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    level_solved = {}

    for difficulty in problems:
        for category in usr_data['category_count']:
#           print(usr_data['category_count'][category])
            if difficulty in usr_data['category_count'][category]:
                if difficulty not in level_solved:
                    level_solved[difficulty] = int(usr_data['category_count'][category][difficulty])
                else:
                    level_solved[difficulty] += int(usr_data['category_count'][category][difficulty])  

    read_file = open("problem_set/problem_set.pkl", "rb")
    problem_set = pickle.load(read_file)

    all_categories = list(problem_set.keys())
    
    shuffle(all_categories)
    # print(all_categories) 

    recommended_questions = []

    for cat in all_categories:
        person_lvl = 'A'
        if cat in usr_data['category_count']:
            person_lvl = suggested_q_level(get_avg_level(usr_data['category_count'][cat]))
        for q in problem_set[cat]:
            if q[2]==person_lvl and ((str(q[1])+str(q[2])) not in usr_data['cf_solved_problems']):
                if len(recommended_questions)>10:
                    break
            
                recommended_questions.append(q)
        if len(recommended_questions)>10:
            break

    return recommended_questions


if __name__ =="__main__":
    print(recommend_q("parvg555"))