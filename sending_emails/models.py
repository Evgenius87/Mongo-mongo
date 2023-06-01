import certifi
from mongoengine import *


uri = "mongodb+srv://errormaker:AT90Ity1AmlqFEFK@honey.0t39yjj.mongodb.net/?retryWrites=true&w=majority"
connection = connect(host=uri,  tlsCAFile=certifi.where(), ssl=True)


class Contact(Document):

    name = StringField(max_length=100, min_length=4)
    email = StringField(max_length=40, min_length=4)
    is_delivered = BooleanField(default=False)
