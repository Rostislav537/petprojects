from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def mainp():
    return render_template("main.html")


@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/add/hand")
def addhand():
    return render_template("handtype.html")

@app.route("/about")
def aboutp():
    return "hy"

@app.route("/api/get")
def api(apikey, base):
    return apikey+base


@app.route("/api/add/", methods=["POST", "GET"])
def apiadd():
    print(request.files)
    return request.form["title"]

if __name__=="__main__":
    app.run(debug=True)
