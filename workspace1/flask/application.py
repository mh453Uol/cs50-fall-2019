from flask import Flask, render_template, request
import os
import csv

secret = os.getenv("secret")

app = Flask(__name__)

students = []

model = {
    "name": "",
    "dorm": "",
    "errors": True
}

@app.route("/")
def index():
    model = {}
    model["errors"] = True
    print(f" Secret: {secret}")
    return render_template("index.html", model=model)

@app.route("/person", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    model["name"] = name
    model["dorm"] = dorm

    if not name or not dorm:
        model["errors"] = True
        return render_template("index.html", model=model)
    else:
        model["errors"] = False

        file = open("registered.csv", "a")
        writer = csv.writer(file)
        writer.writerow((name, dorm))
        file.close()

        return render_template("index.html", model=model)

@app.route("/people")
def people():
    students = []
    with open("registered.csv", "r") as file:
        for line in file.readlines():
            content = line.strip().split(",")
            students.append({ "name":content[0], "dorm": content[1] })

    return render_template("people.html",students=students)