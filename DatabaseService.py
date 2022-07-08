# pip install --upgrade firebase-admin
# pip3 install firebase-admin
# Documentation to use firestore https://firebase.google.com/docs/firestore/manage-data/add-data
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
        self.getRecord()

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
        self.documentName = dictionaryObject["DOCID"].strip() #removes whitespace
        self.key = dictionaryObject["KEY"].strip()
        if(newUser):
            self.createInitialRecord()

    def updateHighScore(self,score):
        if score > self.highScore:
            self.highScore = score
            firestore.client().collection(u"Users").document(self.documentName).update({"highScore" : score})

    def updateHighestLevel(self, level):
        self.highestLevel = level
        firestore.client().collection(u"Users").document(self.documentName).update({"highestLevel" : level})

    def updateKey(self, key):
        self.key = key
        firestore.client().collection(u"Users").document(self.documentName).update({"key" : key})

    def updateName(self, name):
        self.name = name
        firestore.client().collection(u"Users").document(self.documentName).update({"name" : name}) # change name in database
        
   
    def getRecords(self): # get all records
        db = firestore.client()
        docs = db.collection(USERS).stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')

    def getRecord(self): # Saves cloud data locally into variables
        db = firestore.client()
        localdoc_ref = db.collection(u'Users').document(self.documentName).get()
        info = localdoc_ref.to_dict()
        self.name = info["name"]
        self.highestLevel = info["highestLevel"]
        self.highScore = info["highScore"]

    def getScoreBoard(self):
        db = firestore.client()
        highScores ={}
        localdoc_ref = db.collection(u'Users').order_by(u"highScore",direction=firestore.Query.DESCENDING).limit(5).stream() #highest 5 scores
        for doc in localdoc_ref:
            data = doc.to_dict()
            highScores[doc.id] =  data["highScore"],":", data["name"]
        return(highScores) # Returns a dictionary with the doc id as the key and the name:highscore as the value
    
        pass
    def checkLevelUpdate(self,level):
        if(level > self.highestLevel):
            self.updateHighestLevel(level) 

        
        
        


