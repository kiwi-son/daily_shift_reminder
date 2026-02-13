import yagmail
from datetime import datetime, timedelta
from collec import *
import os

EMAIL_ID = os.getenv("EMAIL_ID")
EMAIL_PASS = os.getenv("EMAIL_PASS")
utc_now = datetime.utcnow()
ist_now = utc_now + timedelta(hours=5, minutes=30)
dt = ist_now
def send_email(email, msg):
    sender = EMAIL_ID
    password = EMAIL_PASS  # Gmail App Password
    receiver = email

    yag = yagmail.SMTP(sender, password)
    yag.send(
        to=receiver,
        subject=f"Shift Man power of NCU-AU Instrumentation",
        contents=msg
    )

for i in range(len(user_name)):
    print(shift[i])
    msg=""
    if shift[i] in ["PH", "RH", "//", "L", "SG", "SS"]:
        continue
    elif shift[i]==None:
        msg=f"""
        Hey, {user_name[i]},
        No shift schedule!!! Please Upload shift schedule.
        """
    else:
        msg=f"""
        Date: {dt.day}/{dt.month}/{dt.year}
        Shift: {shift[i]}
        Shift Engineer (Inst): {user_name[i]} 
        Shift Technicians (Inst): {", ".join (manpower[i])} 
        Contact No.: 2844 / 2853 / {user_mobile[i]}
        """

    send_email(user_email[i], msg)




