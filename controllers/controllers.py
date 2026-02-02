# import all the packages 

from flask import request,jsonify,render_template

from config.db import db
from models.db_model import Single_Task

# ========= controllers ===============

# get all tasks or get all tasks based on filter

def tasks():
    if request.method == "GET":
        status = request.args.get("status")
        q = request.args.get("q")
        sort = request.args.get("sort")

        query = Single_Task.query

        if status:
            query = query.filter_by(status=status)
        if q:
            query = query.filter(Single_Task.title.ilike(f"%{q}%"))
        if sort:
            if sort == "asc":
                query = query.order_by(Single_Task.created_at.asc())
            elif sort == "desc":
                query = query.order_by(Single_Task.created_at.desc())

        allTasks = query.all()
        tasks_list = [task.to_dict() for task in allTasks]

        return render_template("all_tasks.html", tasks=tasks_list)

    else:
        # POST request: use keyword arguments
        title = request.form.get("title")
        description = request.form.get("description")
        status = request.form.get("status", "todo")
        due_date = request.form.get("due_date") 

        task = Single_Task(
            title=title,
            description=description,
            status=status,
            due_date=due_date
        )

        db.session.add(task)
        db.session.commit()

        return render_template("task.html",task=task)



# get a specifc task base on it's id 

def specific_task(id):

    specificTask = Single_Task.query.filter_by(id=id).first()

    if not specificTask:
        return jsonify({"error": "Task not found"}), 404

    if request.method == "GET" :
        return jsonify({
        "message" : f"The task of id : {id}" ,
        "value": specificTask.to_dict()
        })
    elif request.method == "DELETE":
        
        db.session.delete(specificTask)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Task deleted successfully",
            "deleted_id": id
        }), 200



# update a specific task based on its id

def update_task(id):
    specificTask = Single_Task.query.filter_by(id=id).first()

    if not specificTask:
        return jsonify({"error": "Task not found"}), 404

    # Get JSON data from request
    data = request.get_json()
    
    # Update fields if provided
    if 'title' in data:
        specificTask.title = data['title']
    if 'description' in data:
        specificTask.description = data['description']
    if 'status' in data:
        specificTask.status = data['status']
    if 'due_date' in data:
        specificTask.due_date = data['due_date']
    
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Task updated successfully",
        "task": specificTask.to_dict()
    }), 200



