import pymongo

# DEFAULT DB CONFIGURATIONS
DB_NAME = "docs"
DB_PASS = "chirayu911"

# DEFAULT MySQL CONNECTION CONFIGURATIONS
URI = "mongodb+srv://chirayu:" + DB_PASS + "@docs.hxuvi.mongodb.net/" + DB_NAME + "?retryWrites=true&w=majority"
CLIENT = pymongo.MongoClient(URI)

# CONNECTION TO DB_DOCTORS_AND_PATIENTS
db = CLIENT.medblock

# DB_CURSOR OBJECT
patients = db.patients
doctors = db.doctors
admin = db.admin

