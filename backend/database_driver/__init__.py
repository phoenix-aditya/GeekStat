'''
package to interact with MongoDB database
written using pymongo driver
'''
from .database import database
from .services import (
    insert_documents,
    insert_document,
    check_if_collection_exists,
    check_if_id_in_collection,
    return_latest_doc_in_collection,
    return_doc_by_username,
    update_document_by_username,
    return_unique_values_in_field,
    retrieve_question_set_of_category
)
