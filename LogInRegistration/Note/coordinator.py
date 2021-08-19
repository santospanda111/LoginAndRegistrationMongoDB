from pymongo import MongoClient
from dotenv import dotenv_values

'''.env file configurations'''
config = dotenv_values('.env')

class Note_Coordinator():

    def __init__(self):

        # Here it'll connect the database by using pymongo
        
        self.client = MongoClient(config.get('host'), 27017)
        self.db = self.client[config.get('db')]
        self.collection=self.db[config.get('notes_db')]

    def read_notes(self,data):
        """
            This method is used to read data by user_id.
            :param request: It accepts user_id as parameter.
            :return: It returns the notes information by using user_id.
        """
        all_data=[]
        note_data=self.collection.find({'user_id':data.get('user_id')},{"_id":0})
        for datas in note_data:
            all_data.append(datas)
        return all_data    

    def insert_notes(self,data):
        """
            This method is used to insert data to create new note.
            :param request: It accepts user_id,title and description as parameter.
            :return: It returns True after successful insertion.
        """
        prev_note=self.collection.find({},{'note_id':1,'_id':0}).sort('_id',-1).limit(1)
        prev_note_id=prev_note[0]['note_id']
        inserted_data= self.collection.insert({'title':data.get('title'),'description':data.get('description'),'user_id':data.get('user_id'),'note_id':prev_note_id+1})
        return True

    def update_note(self,data):
        """
            This method is used to update note using note_id.
            :param request: It accepts note_id,user_id,title and description as parameter.
            :return: It returns True after successful updation.
        """

        update_data=self.collection.update({'note_id':data.get('note_id')},{'user_id':data.get('user_id')},{'title':data.get('title'),'description':data.get('description')})
        return True

    def delete_note(self,data):
        """
            This method is used to delete note using user_id.
            :param request: It accepts user_id as parameter.
            :return: It returns True after successful deletion.
        """
        user_id=data.get('user_id')
        delete_all=self.collection.delete_many({'user_id':user_id})
        return True