from model import *


class CreateTable:

    def create_table():
        ConnectDatabase.db.connect()
        ConnectDatabase.db.drop_tables([UserStory], safe=True, cascade=True)
        ConnectDatabase.db.create_tables([UserStory], safe=True)

CreateTable.create_table()
