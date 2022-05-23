from flask import Flask
from pymongo import MongoClient
from cProfile import run
from flask import request


app = Flask(__name__)

@app.route('/login')
def login():
    id = request.args.get('id')
    walletad = request.args.get('walletad')
    cluster=MongoClient("mongodb+srv://Testing:mXogKmnBbBg47fdH@cluster0.nwq7q.mongodb.net/signatures?retryWrites=true&w=majority")
    db = cluster["signatures"]
    collection= db["Sales"]
    post= {"_id":id, "walletad":walletad}
    collection.insert_one(post)
    print(id)
    print(walletad)
    return "Submitted"

app.run(debug=False, host="0.0.0.0")
