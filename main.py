from flask import *
from pymongo import MongoClient
from file_storing_user import storing
from config import MONGO_URI
app = Flask(__name__)
app.secret_key = "secret"


client=MongoClient(MONGO_URI)
db_auth = client["Authentication"]
db_user = client["user"]
db_shift = client["shift"]

@app.after_request
def no_cache(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route("/", methods=["GET"])
def home():
    session.clear()
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    emp=request.form.get('emp-id')
    password=request.form.get('password')
    #print(type(email))
    #print(email, password)
    collection=db_auth['Authentication']
    
    res=collection.find_one({
        'emp':int(emp),
        'pass':password
    })
    #print(res)
    if res==None:
        flash("Invalid email or password", "danger")
        return redirect(url_for("home"))
    session["logged_in"] = True
    session["user"] = emp
    print(db_shift.list_collection_names())
    if not session.get("logged_in"):
        return redirect(url_for("home"))
    if db_shift.list_collection_names()!=[]:
        return render_template("delete.html")
    
    return redirect(url_for("upload_page"))
@app.route("/delete", methods=["POST"])
def delete():
    if not session.get("logged_in"):
        flash("Please login first", "danger")
        return redirect(url_for("home"))
    client.drop_database('shift')
    return redirect(url_for("success"))

@app.route("/upload", methods=["GET"])
def upload_page():
    if not session.get("logged_in"):
        flash("Please login first", "danger")
        return redirect(url_for("home"))
    return render_template("index_1.html")
def check(file):
    ext=["csv", "xlsx"]
    if '.' in file:
        if file.rsplit('.',1)[1].lower() in ext:
            return True
    return False
@app.route("/upload", methods=["POST"])
def upload():
    if not session.get("logged_in"):
        flash("Session expired. Login again.", "danger")
        return redirect(url_for("home"))
    f = request.files.get("file")
    if not f or not check(f.filename):
        flash("Invalid file", "danger")
        return redirect(url_for("upload_page"))
    

    for i in db_user.user.find():
        f.seek(0)
        storing(f, i["name"], i["emp_id"], db_shift[i["name"]])

    return redirect(url_for("success"))

@app.route("/success", methods=["GET"])
def success():
    if not session.get("logged_in"):
        return redirect(url_for("home"))
    session.clear()
    return render_template("submit.html")

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()  
    flash("Logged out successfully", "success")
    return redirect(url_for("home"))


app.run(debug=True)