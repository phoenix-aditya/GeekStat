from email.policy import default
from schematics.models import Model
from schematics.types import ListType, IntType, StringType, DictType, ModelType

class User(Model):
    username = StringType(default = "user does not exist")
    cf_rating = IntType(default = 0)
    cf_max_rating = IntType(default = 0)
    cf_rank = StringType(default = "newbie")

    cf_category_count = DictType(DictType(ListType(IntType, default=[])),default = {}, serialize_when_none=True)
    cf_solved_questions_id = ListType(StringType, default = [], serialize_when_none=True)
    cf_rating_changes = ListType(IntType, default = [], serialize_when_none = True)

    class Options:
        serialize_when_none = True
