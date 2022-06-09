# pip install --upgrade firebase-admin
# pip3 install firebase-admin
# Documentation to use firestore https://firebase.google.com/docs/firestore/manage-data/add-data
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("secrets/pimath-b26d0-firebase-adminsdk-chop6-93f5751222.json")
firebase_admin.initialize_app(cred, {
  'projectId': "pimath-b26d0",
})

db = firestore.client()
USERS = u'Users'
doc_ref = db.collection(USERS).document
class DatabaseService:
    #def __checkExist(self): # Check text file for key and record and deturmine if it exist
     #    pass

    def __init__(self):
        self.users = u'Users' # Never changes, Collection Name
        self.highScore = 0 # Will change once record is fetched from firebase
        self.highestLevel = 0 # Will change once record is fetched from firebase
        self.key = "" # Will fetch from local text file, used to authenticate user
        self.name = "" # Will fetch from server later or will be created on first run
        self.id = "" # document id will be stored in text file locally
        #__checkExist() # Checks if record exist in database by first checking if text file exist
        pass

    def updateDataBase(self):
        pass

    def __createInitialRecord(self): # create if it doesn't exist
        doc_ref.set({ # Set overwrites previous document, use update if it already exist.
        u'highScore': 0,
        u'highestLevel': 0,
        u'key': "", # once the user creates a name generate this variable as 4 letters and 8 digits. Save it in the textfile locally.
        u'name':"", # stored on server
        })      

    def readLocalFile(self):
        dictionaryObject = {}
        fileReader = open('local_data.txt', 'r+') # Read and overwrite possible starting at position 0 https://stackoverflow.com/questions/6648493/how-to-open-a-file-for-both-reading-and-writing
        try:
            for lineData in fileReader:
                dictKey, dictValue = lineData.split(",")
                dictionaryObject[dictKey] = dictValue # convert each line to a dictionary
        except: # Create file and generate new key
            pass 
        finally:
            fileReader.close()
        print(dictionaryObject)
        


    def updateName(self, name): #Change the Name variable
        self.name = name
        updateDataBase()

    def updateHighScore(self,score):
        self.highScore = score
        updateDataBase()

    def updateHighestLevel(self, level):
        self.highestLevel = level
        updateDataBase()

    def updateKey(self, key):
        self.key = key
        updateDataBase()

    def updateName(self, name):
        self.name = name
        updateDataBase()
        
   
    def getRecord(self):
        localdoc_ref = db.collection(USERS).document(self.id)
        doc = localdoc_ref.get()
        if doc.exists:
            print(f'Data: {doc.to_dict()}')
        else:
            print(u'Document Not Found!')
        return {doc.todict()}


db = DatabaseService() 
db.readLocalFile() # reads file line by line. Each comma seperates dictionary key and value.