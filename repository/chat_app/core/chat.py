from mongoengine import *

connect('db_chat')

GENDER = (0, 'F', 'M')

class User(Document):
    login = StringField(required=True)
    name = StringField(max_length=50)
    gender = StringField(max_length=1, choices=GENDER)


class Room(Document):
    name = StringField(required=True)


class RoomPost(Document):
    msg = StringField(max_length=500, required=True)
    #room = ReferenceField(Room)
    author = ReferenceField(User)