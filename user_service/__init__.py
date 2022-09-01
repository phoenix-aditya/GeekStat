'''
The package manages the generation and updation of user details
on the MongoDB database
the information is fetched from codeforces and is used to recommend questions
and also provide various information to the GeekStat Front-end
'''
from .user_service import (
    generate_and_update_user_details
    )
