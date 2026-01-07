import yagmail
from datetime import datetime, timedelta
from collec import *
import os

EMAIL_ID = os.getenv("EMAIL_ID")
EMAIL_PASS = os.getenv("EMAIL_PASS")
utc_now = datetime.utcnow()
ist_now = utc_now + timedelta(hours=5, minutes=30)
dt = ist_now + timedelta(days=1)
def send_email(email, msg):
    sender = EMAIL_ID
    password = EMAIL_PASS  # Gmail App Password
    receiver = email

    yag = yagmail.SMTP(sender, password)
    yag.send(
        to=receiver,
        subject=f"Tomorrow ({dt.day}-{dt.month}-{dt.year}) Shift",
        contents=msg
    )

for i in range(len(user_name)):
    print(shift[i])
    msg=""
    if shift[i] in ["PH", "RH", "//", "L"]:
        msg=f"""
        Hi {user_name[i]}, 
        Tomorrow  is a Holiday 🎉!!!
        No office.

        Enjoy your day!
        """
    else:
        msg=f"""
        Hi {user_name[i]},
        Tomorrow your shift is {shift[i]},
        Manpowers are :- {", ".join (manpower[i])}
    """

    send_email(user_email[i], msg)

