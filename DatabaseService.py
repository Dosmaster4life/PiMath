# pip install --upgrade firebase-admin
# pip3 install firebase-admin
# Documentation to use firestore https://firebase.google.com/docs/firestore/manage-data/add-data
from pickle import TRUE
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random, string
from pathlib import Path


cred = credentials.Certificate("secrets/pimath-b26d0-firebase-adminsdk-chop6-93f5751222.json")
firebase_admin.initialize_app(cred, {
  'projectId': "pimath-b26d0",
})

db = firestore.client()
USERS = u'Users'
doc_ref = db.collection(USERS).document()
class DatabaseService:


    def __init__(self):
        self.documentName = u'' # ID of user
        self.users = u'Users' # Never changes, Collection Name
        self.highScore = 0 # Will change once record is fetched from firebase
        self.highestLevel = 0 # Will change once record is fetched from firebase
        self.key = "" # Will fetch from local text file, used to authenticate user
        self.name = "" # Will fetch from server later or will be created on first run
        self.id = "" # document id will be stored in text file locally
        self.readWriteLocalFile()
        pass

    def updateDataBase(self):
        pass

    def createInitialRecord(self): # create if it doesn't exist
        db = firestore.client() # required to connect
        db.collection(u"Users").document(self.documentName).set({ # Set overwrites previous document, use update if it already exist.
        u'highScore': 0, # stored on server
        u'highestLevel': 0, # stored on server
        u'key': self.key, # Authentication check with this key in the future
        u'name': "", # stored on server
        })      

    def readWriteLocalFile(self): # Works as intended

        checkExist = Path('local_data.txt')
        checkExist.touch(exist_ok=True) # Writes files if it doesn't exist
        newUser = False
        
        dictionaryObject = {}

        fileReader = open('local_data.txt', 'r+') # Read and overwrite possible starting at position 0 https://stackoverflow.com/questions/6648493/how-to-open-a-file-for-both-reading-and-writing
        try:
            for lineData in fileReader:
                dictKey, dictValue = lineData.split(",")
                dictionaryObject[dictKey] = dictValue # convert each line to a dictionary
        except: # Create file and generate new key
               pass
        finally:
                pass
          
        if len(dictionaryObject) < 2:
            dictionaryObject["DOCID"] = doc_ref.id
            dictionaryObject["KEY"] = ''.join(random.sample(string.ascii_letters,4)).join(random.sample(string.digits,8))
            newUser = True
            for key, value in dictionaryObject.items():
                fileReader.write('%s,%s\n' % (key,value))
        fileReader.close()
        self.documentName = dictionaryObject["DOCID"]
        self.key = dictionaryObject["KEY"]
        if(newUser):
            self.createInitialRecord()

    def updateName(self, name): #Change the Name variable
        self.name = name
        self.updateDataBase()

    def updateHighScore(self,score):
        self.highScore = score
        self.updateDataBase()

    def updateHighestLevel(self, level):
        self.highestLevel = level
        self.updateDataBase()

    def updateKey(self, key):
        self.key = key
        self.updateDataBase()

    def updateName(self, name):
        self.name = name
        self.updateDataBase()
        
   
    def getRecord(self): # not tested
        db = firestore.client()
        localdoc_ref = db.collection(USERS).document(self.id)
        doc = localdoc_ref.get()
        if doc.exists:
            print(f'Data: {doc.to_dict()}')
        else:
            print(u'Document Not Found!')
        return {doc.todict()}

db = DatabaseService() # Create user in database if local_data doesn't exist
