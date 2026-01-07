from pymongo import MongoClient
from datetime import datetime, timedelta
import os
MONGO_URI = os.getenv("MONGO_URI")
utc_now = datetime.utcnow()
dt = utc_now + timedelta(hours=5, minutes=30)

tomorrow = (dt + timedelta(days=1)).replace(
    hour=0, minute=0, second=0, microsecond=0
)
client= MongoClient(MONGO_URI)
db=client['user'] #user database
shift_db=client['shift'] #shift schedule database
user=db['user']
user_email=[]
user_name=[]
for i in user.find():
    user_email.append(i.get('email'))
    user_name.append(i.get('name'))
manpower=[]
shift=[]

for i in user_name:
    coll=shift_db[i]
    res=coll.find_one({"date":tomorrow})
    manpower.append(res['manpower'])
    shift.append(res['shift'])



    



