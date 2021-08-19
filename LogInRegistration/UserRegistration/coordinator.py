from pymongo import MongoClient
from datetime import datetime
from dotenv import dotenv_values

'''.env file configurations'''
config = dotenv_values('.env')

class Coordinator():
    
    def __init__(self):

        # Here it'll connect the database by using pymongo

        self.client = MongoClient(config.get('host'), 27017)
        self.db = self.client[config.get('db')]
        self.collection=self.db[config.get('collection')]

    def check_username_present(self,data):
        """
            This method is used to check the username is present or not.
            :param request: It accepts username as parameter.
            :return: It returns the checked_data,username.
        """
        username=data.get('username')
        checked_data=self.collection.find({'username':username}).count()
        return checked_data,username

    def insert_data(self,data):
        """
            This method is used to insert the data to register the user.
            :param request: It accepts first_name,last_name,email,username,password,is_staff,is_active,is_superuser and date_joined as parameter.
            :return: It returns True if data successfully inserted.
        """
        username=data.get('username')
        email=data.get('email')
        inserted_data=self.collection.insert({'first_name':data.get('first_name'),'last_name':data.get('last_name'),'email':email,'username':data.get('username'),'password':data.get('password'),'is_staff':0,'is_active':1,'is_superuser':0,'date_joined':datetime.now()})
        return True