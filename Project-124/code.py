from flask import Flask,jsonify,request
app = Flask(__name__)
@app.route("/")

def hello_juan():
    return "juan"

tasks = [
    {
        "id":1,
        "Name":"Mama",
        "Contact":"174912",
        "done":False,
    }, 
      {
        "id":2,
        "Name":"Joe",
        "Contact":"123123",
        "done":False,
    }
]
@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    contact = {
        "id":tasks[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get["Contact",""],
        "done":False,
    }
    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })
@app.route("/get-data")


def get_task():
    return jsonify({
        "data":tasks
    })


if __name__ == "__main__":
    app.run()
