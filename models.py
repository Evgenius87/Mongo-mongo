
from mongoengine import *
from mongoengine.fields import  EmbeddedDocumentField, ListField, StringField, ReferenceField



class Authors(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField()
    tags = ListField(StringField(max_length=30))



