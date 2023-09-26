
from pymongo import MongoClient
from datetime import datetime
import traceback
import re
from bson.objectid import ObjectId

class Database:
    def __init__(self, collection_name):

        try:
            self.coll = collection_name
            conn = MongoClient("mongodb://localhost:27017/")
            self.db = conn["flask_database"]
        except:
            traceback.print_exc()
            raise ("connection to database failed")
    
    def insert_content(self, content):
        data = {}
        data["content"] = content
        data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
        self.db[self.coll].insert_one(data)

    def get_all(self):
        return self.db[self.coll].find()

    def search_content(self, search_text):
        #self.db[self.coll].create_index([('content', 'text')])
        
        regx = re.compile(f"^{search_text}", re.IGNORECASE)
        return self.db[self.coll].find({ "content": regx })

    def edit_content(self, new_content, note_id):
        target = {'_id': ObjectId(note_id)}
        newValue = { "$set": { 'content': new_content } }
        self.db[self.coll].update_one(target, newValue)

    def delete_content(self, id):
        self.db[self.coll].delete_one({'_id': ObjectId(id)})


    