from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

from controllers.controllers import tasks, specific_task, update_task
from models.db_model import Single_Task
from config.db import db

# Load environment variables
load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# Basic API's for UI
@app.route("/")
def home_controller():
    return render_template("index.html"), 200


@app.route("/add-task")
def get_add_task_controller():
    return render_template("add_task.html"), 200


# Main API's

@app.route("/api/tasks", methods=["GET", "POST"])
def tasks_call():
    return tasks()  


@app.route("/api/tasks/<int:id>", methods=["GET", "DELETE", "PUT"])
def specific_task_call(id):
    if request.method == "PUT":
        return update_task(id)
    return specific_task(id)



# others 

if __name__ == "__main__":
    app.run(debug=True)