'''
Package recommends user questions based on questions solved by user
category wise
'''
import random
from database_driver.services import retrieve_question_set_of_category, update_document_by_username
from models import Problem, User
from database_driver import (
    return_doc_by_username,
    return_unique_values_in_field
    )
from user_service import generate_and_update_user_details
from statistics import mean

def recommend_q_to_user(username:str):
    '''
    function to recommend user questions based
    on the level of user in categories
    the recommender recommends 10 questions in category
    '''
    
    # update user profile on database
    if generate_and_update_user_details(username=username) == False:
        return None

    # retrieve user profile from database
    user = User(
        return_doc_by_username(
        collection_name='users',
        username=username
    ))

    categories = return_unique_values_in_field(
        collection_name='problemset',
        field_name='tags'
    )
    
    list_of_questions = []
    target_categories = random.sample(categories, 5)

    for category in target_categories:
        list_of_avg_ratings = []
        list_of_avg_ratings.append(800)

        if category in user.cf_category_count:
            for lvl in user.cf_category_count[category]:
                list_of_avg_ratings.append(mean(user.cf_category_count[category][lvl]))
        
        level_in_category = max(list_of_avg_ratings)

        # retrieving 1 easy, 2 medium & 1 hard question from category

        list_of_q_from_category = retrieve_question_set_of_category(
            collection_name="problemset",
            category_name=category,
            avg_level_of_user=level_in_category,
            user=user
        )

        selected_questions = random.sample(list_of_q_from_category, min(len(list_of_q_from_category), 5))
        list_of_questions.extend(selected_questions)

    final_recommended_q = random.sample(list_of_questions, 10)

    # update the recommended question set on database
    user.recommended_questions = final_recommended_q
    update_document_by_username(
        collection_name='users',
        username=user.username,
        document=user.to_primitive()
    )

    return final_recommended_q
