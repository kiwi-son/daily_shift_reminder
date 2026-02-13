from pymongo import MongoClient
from datetime import datetime, timedelta
import os
MONGO_URI = os.getenv("MONGO_URI")
utc_now = datetime.utcnow()
dt = utc_now + timedelta(hours=5, minutes=30)

today = dt.replace(
    hour=0, minute=0, second=0, microsecond=0
)
client= MongoClient(MONGO_URI)
db=client['user'] #user database
shift_db=client['shift'] #shift schedule database
user=db['user']
user_email=[]
user_name=[]
user_mobile=[]
for i in user.find():
    user_email.append(i.get('email'))
    user_name.append(i.get('name'))
    user_mobile.append(i.get('mobile'))
manpower=[]
shift=[]

for i in user_name:
    coll=shift_db[i]
    res=coll.find_one({"date":today})
    if res is not None:
        manpower.append(res.get('manpower'))
        shift.append(res.get('shift'))
    else:
        manpower.append(None)   
        shift.append(None)
    coll.delete_many({
        "date":{"$lt" : today}
    })




    







