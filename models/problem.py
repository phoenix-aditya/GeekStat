from schematics.models import Model
from schematics.types import ListType, IntType, StringType

class problem(Model):
    _id = StringType()
    contestID = IntType()
    index = StringType()
    rating = IntType()
    tags = ListType(StringType)

    class Options:
        serialize_when_none = True
